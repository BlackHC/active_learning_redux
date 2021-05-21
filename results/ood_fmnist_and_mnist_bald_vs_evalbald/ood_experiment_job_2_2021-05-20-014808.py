store = {}
store['timestamp']=1621471688
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=2']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=2
store['worker_id']=2
store['num_workers']=80
store['config']={'seed': 1236, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.1934378147125244})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6525511741638184})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.6837615966796875})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.813356637954712})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.9517016410827637})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.724815845489502})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.8380250930786133})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.9290127754211426})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.078594923019409})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.1395223140716553})
store['active_learning_steps'][0]['training']['best_epoch']=7
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6974, 'crossentropy': 2.602639453125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4161242246627808})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4024125337600708})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4282970428466797})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.6493616104125977})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 16756], ['id', 47759], ['id', 1314], ['id', 46329], ['id', 4703]], 'labels': [7, 2, 7, 3, -1], 'scores': [0.9461367262383724, 1.6970776250348902, 2.203285010561043, 2.5164512542098443, 2.6810033270877867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.531409740447998})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.025850534439087})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.803007125854492})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.091292381286621})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6505, 'crossentropy': 2.2942552734375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4166587591171265})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.3697822093963623})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3648157119750977})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 36661], ['id', 6873], ['id', 11191], ['id', 44013], ['id', 4703]], 'labels': [5, 8, 8, 4, -1], 'scores': [0.8204796510495931, 1.4787851302176547, 1.9506758250755345, 2.276168824666473, 2.476673647012891]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.8957278728485107})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.482232093811035})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.5109920501708984})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.752206325531006})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7292, 'crossentropy': 1.640927734375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.3107963800430298})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2993757724761963})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.230491042137146})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 56004], ['id', 7881], ['id', 31777], ['id', 40456], ['id', 22517]], 'labels': [8, 3, 4, 0, 5], 'scores': [0.7006265823357949, 1.2428880226864112, 1.6925739361150631, 2.0049323672896975, 2.207724818714196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.226651191711426})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.5483055114746094})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.7229034900665283})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.986435890197754})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.1613550186157227})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.1083056926727295})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.8357608318328857})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 3.260138988494873})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 3.1740903854370117})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7025, 'crossentropy': 2.633893359375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.5177018642425537})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.5174262523651123})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.4957129955291748})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.5446982383728027})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.7360122203826904})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.583815574645996})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.6178890466690063})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.8294368982315063})
store['active_learning_steps'][3]['eval_training']['best_epoch']=6
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 52538], ['id', 8388], ['id', 34524], ['id', 56877], ['id', 33247]], 'labels': [9, 1, 8, 9, 5], 'scores': [0.8831032854452858, 1.6863504096564155, 2.2941452227513075, 2.6834409804996326, 2.8742389145232643]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.864851951599121})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.319242000579834})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.411865711212158})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.4209604263305664})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.584832191467285})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.5700745582580566})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.94771409034729})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7304, 'crossentropy': 2.166696484375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.2911648750305176})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.4742543697357178})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.5263965129852295})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4681577682495117})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 33274], ['id', 4843], ['id', 26100], ['id', 51398], ['id', 35989]], 'labels': [2, 2, 8, 2, 4], 'scores': [0.8085455543630415, 1.4503423599675362, 1.9358302875290208, 2.226366057084679, 2.4269289349545318]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.385197401046753})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.4990134239196777})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.6328961849212646})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.57785165309906})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.9567818641662598})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 2.005701780319214})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8215, 'crossentropy': 1.27611962890625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.2460711002349854})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.2331575155258179})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.1632559299468994})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0998542308807373})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.095024585723877})
store['active_learning_steps'][5]['eval_training']['best_epoch']=5
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 57985], ['id', 28734], ['id', 36128], ['id', 29290], ['id', 36818]], 'labels': [4, 3, 3, 2, 7], 'scores': [0.7847969190567607, 1.4456633607582052, 1.9355080442326322, 2.294321694218148, 2.5178462127415067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.3745675086975098})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.5326271057128906})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.6239944696426392})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.5694918632507324})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.7279112339019775})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.8802882432937622})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.9190542697906494})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8107, 'crossentropy': 1.3055005859375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.2510771751403809})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.1486363410949707})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.0806632041931152})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.08544921875})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0261790752410889})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.023329257965088})
store['active_learning_steps'][6]['eval_training']['best_epoch']=6
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 46435], ['id', 9468], ['id', 36337], ['id', 1364], ['id', 54898]], 'labels': [9, 6, 3, 9, 3], 'scores': [0.8610550268542675, 1.5222946446583765, 2.077269396711702, 2.431644812167293, 2.65704483096897]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.2550443410873413})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.4717273712158203})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.5973323583602905})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.6964348554611206})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.7984968423843384})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.7907825708389282})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.9031875133514404})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8005, 'crossentropy': 1.483669921875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.2696926593780518})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.1465582847595215})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.1549558639526367})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.1024417877197266})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.1439368724822998})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.1546437740325928})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 21242], ['id', 16298], ['id', 36662], ['id', 38197], ['id', 8517]], 'labels': [0, 2, 2, 2, 7], 'scores': [0.9302005366555288, 1.6638398237405192, 2.3039282368605862, 2.6911733249733256, 2.968497313698494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4560976028442383})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.8054912090301514})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.836233139038086})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.9814515113830566})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.034576416015625})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.9122909307479858})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.8886656761169434})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 2.337151527404785})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.407318592071533})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8087, 'crossentropy': 1.48343095703125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.4412990808486938})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.3727848529815674})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.3446214199066162})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.3082730770111084})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2428768873214722})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.2797846794128418})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.261784315109253})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.2590277194976807})
store['active_learning_steps'][8]['eval_training']['best_epoch']=7
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 42774], ['id', 33610], ['id', 29079], ['id', 37271], ['id', 43478]], 'labels': [4, 9, 6, 3, 9], 'scores': [0.8519027202103042, 1.495043109471661, 2.013209213778757, 2.3142288690078567, 2.511253348002831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.4136791229248047})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3919720649719238})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.548966646194458})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.6436851024627686})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.718928337097168})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.7066627740859985})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.7458205223083496})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.7923035621643066})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8274, 'crossentropy': 1.34867919921875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.1811330318450928})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0806522369384766})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.095841884613037})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0468741655349731})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0057231187820435})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9883482456207275})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.038017749786377})
store['active_learning_steps'][9]['eval_training']['best_epoch']=7
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 7726], ['id', 26522], ['id', 49300], ['id', 49159], ['id', 44761]], 'labels': [4, 2, 3, 7, 4], 'scores': [0.8980600427364747, 1.5275839779739127, 2.0209223315544125, 2.372642720889524, 2.6086809882784476]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.2642996311187744})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.266571283340454})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.5138123035430908})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.52024245262146})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.601503610610962})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8334, 'crossentropy': 1.016251171875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0459387302398682})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9114726781845093})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8763541579246521})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8479282259941101})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 5303], ['id', 23738], ['id', 26034], ['id', 52971], ['id', 20991]], 'labels': [-1, 9, 5, 2, -1], 'scores': [0.7266052291440972, 1.3547519392547027, 1.8822318820743593, 2.2230641861222873, 2.4182939987284904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1559607982635498})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2644821405410767})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.409471035003662})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.3260304927825928})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4522424936294556})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.4864801168441772})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4912171363830566})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8455, 'crossentropy': 1.07768388671875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.0493923425674438})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9932239651679993})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0432944297790527})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.952741265296936})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9955999255180359})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.031120777130127})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 24584], ['id', 32010], ['id', 28845], ['id', 36897], ['id', 26217]], 'labels': [3, 2, 5, 4, -1], 'scores': [0.8207762404764793, 1.479315633403496, 2.015968696546145, 2.4194015578527126, 2.671889603010535]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.1667546033859253})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1711088418960571})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3309576511383057})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.356231689453125})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4651014804840088})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.433502197265625})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.549985647201538})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.5726951360702515})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.5458661317825317})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.6138129234313965})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.6022316217422485})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.781296968460083})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.546412467956543})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.6436560153961182})
store['active_learning_steps'][12]['training']['best_epoch']=11
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8601, 'crossentropy': 1.2429125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9641505479812622})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9912989139556885})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9878778457641602})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0094705820083618})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9901649951934814})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9774563312530518})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 9660], ['id', 7924], ['id', 44927], ['id', 31688], ['id', 27738]], 'labels': [7, 8, 7, 2, 4], 'scores': [0.9266571066897299, 1.5947365834562315, 2.1283833844767006, 2.5241720200019744, 2.795627498442733]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1631531715393066})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2139363288879395})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3059345483779907})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.3361876010894775})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.412034511566162})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.5863343477249146})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8523, 'crossentropy': 1.03661923828125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0008633136749268})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0088160037994385})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9283570647239685})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9198305010795593})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9232499599456787})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 12061], ['id', 37453], ['id', 39320], ['id', 23863], ['id', 274]], 'labels': [9, 5, 6, 9, 6], 'scores': [0.699032295470262, 1.3175455505802938, 1.8420296843774482, 2.232269236967679, 2.515739644716468]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9837963581085205})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0358195304870605})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0401902198791504})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0123004913330078})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1562453508377075})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2313779592514038})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.2444193363189697})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.189626932144165})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.3438663482666016})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2699201107025146})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8649, 'crossentropy': 1.06911845703125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0192041397094727})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.975378155708313})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9173579216003418})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8608503341674805})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.880913496017456})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8258682489395142})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8834191560745239})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 57728], ['id', 19702], ['id', 27668], ['id', 22136], ['id', 27325]], 'labels': [9, 5, -1, 8, 9], 'scores': [0.8797354477933468, 1.5028465354743141, 1.971880497478363, 2.3227989670120133, 2.6026414783245517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0491368770599365})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.014096736907959})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.017128825187683})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0394073724746704})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0819814205169678})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.2630715370178223})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8722, 'crossentropy': 0.8793638671875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.0182814598083496})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8397403359413147})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7983742356300354})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7883679270744324})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7210636734962463})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 41445], ['id', 42085], ['id', 9414], ['id', 58990], ['id', 56519]], 'labels': [0, 5, 5, 8, 6], 'scores': [0.6772150476301999, 1.2704138419581765, 1.6846412646544167, 1.9540430827964226, 2.1236221917188303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9183468818664551})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8547245264053345})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8902393579483032})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7922744750976562})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0374302864074707})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9161399006843567})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9813709259033203})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8987, 'crossentropy': 0.733701220703125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.959709882736206})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6960560083389282})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6255209445953369})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6511121988296509})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6036924719810486})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5344825983047485})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 30853], ['id', 36452], ['id', 17631], ['id', 20135], ['id', 16911]], 'labels': [5, 5, 5, 1, 3], 'scores': [0.7177868885432492, 1.3163858496716312, 1.760525478004658, 2.102769389819521, 2.321371202380705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9609405994415283})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.837875485420227})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8424685001373291})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9377358555793762})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0058646202087402})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8793, 'crossentropy': 0.754978173828125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9195746779441833})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7016007900238037})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.685828685760498})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6048747897148132})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 55591], ['id', 51696], ['id', 15947], ['id', 52097], ['id', 56174]], 'labels': [5, 6, 3, 1, 0], 'scores': [0.7029720125039434, 1.303981786108967, 1.773139446326697, 2.1129221915568923, 2.338609951995233]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9039580225944519})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8254998326301575})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8976341485977173})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8549961447715759})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9065045714378357})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8902847766876221})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9675366878509521})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8610808849334717})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9914746880531311})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.1310021877288818})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9689430594444275})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9039, 'crossentropy': 0.7413744140625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9357353448867798})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7458142042160034})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6843334436416626})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5936874151229858})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5835466980934143})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6039292812347412})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5919743776321411})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 13627], ['id', 47870], ['id', 12874], ['id', 37969], ['id', 38513]], 'labels': [2, 9, 3, 2, 5], 'scores': [0.8098791603487703, 1.496148279819891, 1.9544466336155457, 2.2834771484214755, 2.4731098090742947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8272511959075928})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8290101289749146})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7741906642913818})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7484368681907654})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7083752155303955})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8058271408081055})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9532498121261597})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9018452167510986})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.917, 'crossentropy': 0.61701083984375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9147739410400391})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7316375970840454})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6518973112106323})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6278048753738403})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6006388664245605})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.593275249004364})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5702598094940186})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 20169], ['id', 972], ['id', 56414], ['id', 9979], ['id', 18328]], 'labels': [4, 8, -1, 2, -1], 'scores': [0.611057255463523, 1.1718465658571604, 1.657136250693858, 2.0333809654707116, 2.3278670184900827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8087376356124878})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7455980777740479})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7797853350639343})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7516195774078369})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8202186822891235})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8508214950561523})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7946367859840393})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8974, 'crossentropy': 0.7261515625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9194992780685425})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7040166258811951})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.594976544380188})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5903393030166626})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5627307295799255})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5720083713531494})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 18598], ['id', 44603], ['id', 52142], ['id', 27712], ['id', 51863]], 'labels': [9, 0, 2, 0, 9], 'scores': [0.7650375292547749, 1.4042834577358825, 1.8579751962383861, 2.2007330923974986, 2.4360638805511075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9451487064361572})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8486233949661255})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.771969199180603})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8081185221672058})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9189510345458984})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9288533926010132})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0167217254638672})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8907, 'crossentropy': 0.71919619140625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8580929636955261})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6891897916793823})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6000381708145142})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5699854493141174})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5478214025497437})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5437296032905579})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 35433], ['id', 19959], ['id', 18962], ['id', 40766], ['id', 51351]], 'labels': [6, 5, 7, 4, -1], 'scores': [0.6974341282664214, 1.299082047752721, 1.7907826230189787, 2.13735767560841, 2.3572433737725635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8598618507385254})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7718873023986816})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6635276675224304})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.71195387840271})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7784985303878784})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8370649218559265})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.608613427734375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7590813636779785})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5964531898498535})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6420873403549194})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5290366411209106})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5197882056236267})
store['active_learning_steps'][22]['eval_training']['best_epoch']=2
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 40390], ['id', 28898], ['id', 45439], ['id', 26516], ['id', 8812]], 'labels': [0, 6, 2, 6, 0], 'scores': [0.7209903160864862, 1.3292263849943664, 1.7994540307701063, 2.1357454585183895, 2.349244389097322]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.899213433265686})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6734191179275513})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7877660989761353})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6834498643875122})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7753034830093384})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7647638320922852})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7567044496536255})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8267735242843628})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8698875308036804})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9129, 'crossentropy': 0.6417548828125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8044298887252808})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5942909717559814})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5739507675170898})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5845202207565308})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.516791820526123})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5123055577278137})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5056152939796448})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.49791425466537476})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 11534], ['id', 48875], ['id', 14394], ['id', 4360], ['id', 32368]], 'labels': [7, 8, 3, 6, -1], 'scores': [0.7722191817678994, 1.4152183624754633, 1.941313357150976, 2.2924610955191875, 2.4845280322670735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8087249994277954})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6596159934997559})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6163604259490967})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7028064727783203})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6326953172683716})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7297282218933105})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7484205961227417})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7385404706001282})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9077, 'crossentropy': 0.665024609375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8636817336082458})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6378079056739807})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.574487566947937})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5141505002975464})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5369824767112732})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.516739547252655})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5001887083053589})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 54167], ['id', 52590], ['id', 39074], ['id', 48323], ['id', 16939]], 'labels': [-1, -1, -1, 2, 9], 'scores': [0.7247782243287857, 1.3557277546129494, 1.8917797200788744, 2.2754031642194743, 2.4753481412388876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9134763479232788})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6484088897705078})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7090364694595337})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7868406772613525})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7478609681129456})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7824792861938477})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8070287704467773})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8202173709869385})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7805147171020508})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7888568639755249})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.761542558670044})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7747827768325806})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8118003606796265})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9299105405807495})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.1048415899276733})
store['active_learning_steps'][25]['training']['best_epoch']=12
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9215, 'crossentropy': 0.6792474609375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8530077934265137})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6308073997497559})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5949462652206421})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5676177740097046})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5689564943313599})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5086938142776489})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5287261009216309})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5317686796188354})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5002670288085938})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 52889], ['id', 42787], ['id', 11643], ['id', 47513], ['id', 26434]], 'labels': [-1, 4, 5, 0, 2], 'scores': [0.836138889031405, 1.5296359622637477, 2.032210617643866, 2.377061056912989, 2.6129195479356566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9091929793357849})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7114875316619873})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6490947008132935})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6995484232902527})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6865715384483337})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7484139204025269})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7677031755447388})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7602874040603638})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.572010546875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0324718952178955})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6682983040809631})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5583958029747009})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5388562679290771})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.533847451210022})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.49101394414901733})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 22083], ['id', 42343], ['id', 8859], ['id', 42001], ['id', 12430]], 'labels': [2, 3, 8, 2, 3], 'scores': [0.5855640186463136, 1.1325101280541885, 1.5662681861271217, 1.8395811929341184, 2.030941040364003]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8700153231620789})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5699754953384399})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6344166994094849})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6908373236656189})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7280470132827759})
store['active_learning_steps'][27]['training']['best_epoch']=2
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9178, 'crossentropy': 0.515169140625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.9081354141235352})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6042134761810303})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5823787450790405})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5375369191169739})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 36421], ['id', 51019], ['id', 1075], ['id', 8093], ['id', 30123]], 'labels': [3, 0, 7, 0, 0], 'scores': [0.5393157733893812, 0.9980977216421847, 1.385634197810039, 1.6986738144669058, 1.938165527201173]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8586435317993164})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6150480508804321})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5687046051025391})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5860849618911743})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5193194150924683})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6111087799072266})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6956565380096436})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7269629240036011})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6731840968132019})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9307, 'crossentropy': 0.5383814453125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.910825252532959})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5694265365600586})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.525188684463501})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4806233048439026})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4884287714958191})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.45705825090408325})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4827525019645691})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4487786293029785})
store['active_learning_steps'][28]['eval_training']['best_epoch']=8
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 26568], ['id', 31624], ['id', 21370], ['id', 56866], ['id', 48735]], 'labels': [-1, 9, 3, 8, -1], 'scores': [0.7685076100721386, 1.463275803768897, 1.9787474817320252, 2.2971001726593725, 2.474725161713234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9163078665733337})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6074674129486084})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5381038188934326})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5994737148284912})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6639660596847534})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6590834856033325})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.508098974609375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8934142589569092})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.620481014251709})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5482475757598877})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.49928757548332214})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5020774602890015})
store['active_learning_steps'][29]['eval_training']['best_epoch']=4
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 31293], ['id', 33222], ['id', 21700], ['id', 31347], ['id', 42070]], 'labels': [8, 5, 7, 3, 3], 'scores': [0.6490984030205202, 1.2195119989857117, 1.6546668430075515, 1.9633445180079443, 2.139553929737148]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8766904473304749})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5944717526435852})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5618662238121033})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5659974813461304})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5908112525939941})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6424826979637146})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9241, 'crossentropy': 0.52078984375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8778530359268188})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6298476457595825})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5147933959960938})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5010983943939209})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5113707780838013})
store['active_learning_steps'][30]['eval_training']['best_epoch']=3
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 14749], ['id', 14760], ['id', 36408], ['id', 12343], ['id', 18846]], 'labels': [0, 2, 1, 4, 4], 'scores': [0.6404557873100103, 1.1746732966571098, 1.6270118691172444, 1.9440595941142655, 2.171059075585389]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8767692446708679})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5468723773956299})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5260859727859497})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5544468760490417})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5037260055541992})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.570003092288971})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.570315420627594})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5620041489601135})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5574224591255188})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6449342370033264})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5957103371620178})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.653557300567627})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9403, 'crossentropy': 0.49998310546875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8425093293190002})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5735257267951965})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5019785761833191})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.41193699836730957})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.39191582798957825})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.40709173679351807})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.3902474343776703})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 45602], ['id', 14762], ['id', 41960], ['id', 48668], ['id', 22002]], 'labels': [5, 9, 3, 8, 3], 'scores': [0.802222519935912, 1.4400558154882248, 1.9760241689419562, 2.3566782749430564, 2.5859663472384944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8901300430297852})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6183689832687378})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5980842113494873})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5252048969268799})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5315863490104675})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5906786918640137})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6533330678939819})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7217797040939331})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.59599769115448})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6441395282745361})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7033689618110657})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6114161014556885})
store['active_learning_steps'][32]['training']['best_epoch']=9
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9376, 'crossentropy': 0.54547041015625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8507633209228516})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5135664939880371})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4650990962982178})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4408882260322571})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4494835138320923})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.423098623752594})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4137730598449707})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 57315], ['id', 40046], ['id', 28499], ['id', 26098], ['id', 14245]], 'labels': [8, 7, -1, 5, 7], 'scores': [0.7630873641149865, 1.421850384940273, 1.910814448777744, 2.2559011001836407, 2.463234577160108]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8945577144622803})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5378013253211975})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.525546669960022})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5878018140792847})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5807887315750122})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5299615859985352})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5531842112541199})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5358213782310486})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5772134065628052})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5684736967086792})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6134792566299438})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6281198263168335})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6871066689491272})
store['active_learning_steps'][33]['training']['best_epoch']=10
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9386, 'crossentropy': 0.509853759765625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8040437698364258})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5344067811965942})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4920716881752014})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4640481770038605})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.46513742208480835})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.42833828926086426})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4161560535430908})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.40420302748680115})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.40439820289611816})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.37197035551071167})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4005976915359497})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 18193], ['id', 32276], ['id', 31989], ['id', 55513], ['id', 42264]], 'labels': [-1, 3, -1, 5, 3], 'scores': [0.7322863328872691, 1.345338603471919, 1.8163769425688887, 2.1430112272165323, 2.3533040914442163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.9786479473114014})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5910623669624329})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48102784156799316})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5180761218070984})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5577958822250366})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4890722334384918})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5453705787658691})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5605762004852295})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5832191109657288})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9425, 'crossentropy': 0.43353486328125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8615023493766785})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5267791748046875})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4457140564918518})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4332233667373657})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4167841672897339})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.41017359495162964})
store['active_learning_steps'][34]['eval_training']['best_epoch']=3
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 14329], ['id', 48973], ['id', 48038], ['id', 54104], ['id', 29360]], 'labels': [0, 8, 3, 0, 8], 'scores': [0.5843350379610532, 1.1178669471498242, 1.5341248612884142, 1.8740172742739034, 2.102486103640839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9142177104949951})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5684767961502075})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5712645053863525})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5771235823631287})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4968603253364563})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5543226003646851})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5671502351760864})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.604181170463562})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9393, 'crossentropy': 0.43896064453125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8300095796585083})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5677937865257263})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.42810606956481934})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3982918858528137})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.39940762519836426})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3912919759750366})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4032060503959656})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 59468], ['id', 31939], ['id', 18053], ['id', 35834], ['id', 43609]], 'labels': [7, 9, -1, -1, 8], 'scores': [0.617553464627669, 1.1630140777802818, 1.6024930246606104, 1.9388386245695894, 2.188700302927998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8163760304450989})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5129728317260742})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4553162455558777})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4710277318954468})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4965577721595764})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49361705780029297})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4972972869873047})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5387960076332092})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.49893441796302795})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5463146567344666})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5302633047103882})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5172373056411743})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9487, 'crossentropy': 0.42871005859375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8914496302604675})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5977551937103271})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.47304806113243103})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4491940140724182})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4011319875717163})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3949680030345917})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4037507176399231})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.37649863958358765})
store['active_learning_steps'][36]['eval_training']['best_epoch']=5
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 11377], ['id', 26568], ['id', 17530], ['id', 57972], ['id', 44424]], 'labels': [3, -1, 8, 4, 2], 'scores': [0.7378516575081735, 1.4053851704194962, 1.907114330905646, 2.2398343498532496, 2.4404010189891343]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.92315673828125})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5567255020141602})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4540916681289673})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47809863090515137})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5216667056083679})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4667772948741913})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.425633642578125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9151203632354736})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5933754444122314})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5027831196784973})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5130242109298706})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.48341935873031616})
store['active_learning_steps'][37]['eval_training']['best_epoch']=4
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 12702], ['id', 46412], ['id', 4153], ['id', 14072], ['id', 53156]], 'labels': [3, 0, 2, 6, 3], 'scores': [0.6729326646087466, 1.197971803495029, 1.6441839810663783, 1.9828801343607276, 2.2220109278544173]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.926558256149292})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5627686977386475})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4643189311027527})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4514787197113037})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.416576623916626})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5337153673171997})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45479124784469604})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9433, 'crossentropy': 0.419008984375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9742449522018433})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5398995876312256})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49795693159103394})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.41660088300704956})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4163762927055359})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.40372157096862793})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 5315], ['id', 48102], ['id', 52886], ['id', 28657], ['id', 44447]], 'labels': [3, 7, 7, 5, -1], 'scores': [0.6474056754665618, 1.2411638127568025, 1.7135886249862722, 2.066209670920875, 2.29782255394678]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8834920525550842})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5060834884643555})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45527029037475586})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4805324077606201})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4957437515258789})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.49762654304504395})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5010536313056946})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4752788543701172})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9445, 'crossentropy': 0.4358443359375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9592463970184326})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5715255737304688})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4595962464809418})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45384079217910767})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4363235831260681})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4225817024707794})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.44730669260025024})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 9789], ['id', 43126], ['id', 2765], ['id', 17358], ['id', 55390]], 'labels': [8, 3, 0, 8, 6], 'scores': [0.5855593616169013, 1.1115485983486506, 1.5503925277954975, 1.8557722566166266, 2.081950203752096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8514480590820312})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5202714204788208})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5318447351455688})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5234658122062683})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4905673563480377})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9316, 'crossentropy': 0.51519892578125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0299561023712158})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6685769557952881})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5818403959274292})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6016973853111267})
store['active_learning_steps'][40]['eval_training']['best_epoch']=3
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 43648], ['id', 53077], ['id', 31301], ['id', 41108], ['id', 4058]], 'labels': [5, 0, 5, 0, 8], 'scores': [0.5789415200665253, 1.077920196364865, 1.4785617341587516, 1.7957406858332643, 2.0297192611228425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0723927021026611})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6584600210189819})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.513603925704956})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5301668643951416})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4563721716403961})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4920254349708557})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5239918231964111})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4492487907409668})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5293607711791992})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.548866868019104})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5068364143371582})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9527, 'crossentropy': 0.3783275146484375}
