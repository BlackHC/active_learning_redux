store = {}
store['timestamp']=1621477916
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=50']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=50
store['worker_id']=50
store['num_workers']=80
store['config']={'seed': 1287, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6182761192321777})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.965447187423706})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.18463397026062})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.186572790145874})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.7109899520874023})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6599, 'crossentropy': 2.59486171875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4374589920043945})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.5633807182312012})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.455391526222229})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.5416734218597412})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 36475], ['id', 19219], ['id', 4727], ['id', 9037], ['id', 31030]], 'labels': [2, 5, 8, 3, 8], 'scores': [1.03204029583805, 1.8654393772728302, 2.437848700522279, 2.8106347056414753, 3.0298910942937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.232630729675293})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.542837619781494})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.8633806705474854})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.670759916305542})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.8206377029418945})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 3.0448951721191406})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.9088940620422363})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.763993740081787})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7162, 'crossentropy': 2.50481953125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4809736013412476})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4648163318634033})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.5673834085464478})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.6209574937820435})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 55244], ['id', 18519], ['id', 57249], ['id', 1301], ['id', 12757]], 'labels': [7, 4, 4, 2, 7], 'scores': [0.8998405172973232, 1.6593356427787422, 2.180468983668171, 2.5344329537053882, 2.7140012038943944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.0309090614318848})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.1967337131500244})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.5386831760406494})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.7256715297698975})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7403, 'crossentropy': 1.6887337890625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3302949666976929})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.2169865369796753})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2382105588912964})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 32550], ['id', 5740], ['id', 12202], ['id', 45380], ['id', 21397]], 'labels': [0, 9, 9, -1, 5], 'scores': [0.8128337736114077, 1.4741936510060785, 2.003046930592446, 2.323338858248393, 2.5456054268906385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.5518929958343506})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.7998416423797607})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.8402652740478516})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.219663619995117})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.2139339447021484})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.080366611480713})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.041415214538574})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.9407436847686768})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.3847482204437256})
store['active_learning_steps'][3]['training']['best_epoch']=6
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7568, 'crossentropy': 1.8305654296875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.299325942993164})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3631693124771118})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.3476804494857788})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.3507235050201416})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.4612183570861816})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.4124042987823486})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.3829503059387207})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 49784], ['id', 19569], ['id', 3370], ['id', 25747], ['id', 42749]], 'labels': [5, 2, 4, 5, 8], 'scores': [0.9033283802842069, 1.662667030182048, 2.208455324125902, 2.5774519328815364, 2.787722348322746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.7141709327697754})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.7155818939208984})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.3093295097351074})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.2425761222839355})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.9136924743652344})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7775, 'crossentropy': 1.3960978515625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.2729192972183228})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.1614675521850586})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.0844600200653076})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0868619680404663})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 29390], ['id', 1149], ['id', 16692], ['id', 27355], ['id', 21040]], 'labels': [9, 4, 5, 6, 9], 'scores': [0.7785688420758963, 1.4105749423230138, 1.8595124462069386, 2.1741833586433925, 2.381339353274665]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.513322353363037})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.88211989402771})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.002331256866455})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.0291507244110107})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.016357898712158})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.239071846008301})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.7068028450012207})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.226036310195923})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.634854793548584})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.3083574771881104})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.5713043212890625})
store['active_learning_steps'][5]['training']['best_epoch']=8
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7801, 'crossentropy': 1.8147193359375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.1888021230697632})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.3386740684509277})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.374049186706543})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.1983668804168701})
store['active_learning_steps'][5]['eval_training']['best_epoch']=1
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 19554], ['id', 23441], ['id', 7808], ['id', 22561], ['id', 59850]], 'labels': [0, 2, 7, 6, 5], 'scores': [0.7828113671132397, 1.4556897251098464, 1.927870842101715, 2.2102893111243658, 2.3927974180971283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3284084796905518})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.751305103302002})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.8995529413223267})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.780935287475586})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.0818963050842285})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.9496299028396606})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 2.1337263584136963})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.9535791873931885})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.9957172870635986})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7847, 'crossentropy': 1.7694134765625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.4434926509857178})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.359433650970459})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.3066473007202148})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.3616433143615723})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.364650011062622})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.3386168479919434})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.2427709102630615})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.3024625778198242})
store['active_learning_steps'][6]['eval_training']['best_epoch']=8
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 53019], ['id', 25695], ['id', 17257], ['id', 41018], ['id', 16844]], 'labels': [2, 3, 3, 6, 5], 'scores': [1.0420503082907793, 1.7837537967392372, 2.3619937111174902, 2.761915979765826, 3.02578074029897]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.2310755252838135})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.210819959640503})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.2539705038070679})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.348126769065857})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.5712878704071045})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.6142876148223877})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.43324613571167})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8305, 'crossentropy': 1.22452587890625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0587620735168457})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9275113940238953})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9631731510162354})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9190261363983154})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9204707145690918})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 1974], ['id', 15947], ['id', 38589], ['id', 49889], ['id', 29573]], 'labels': [8, 3, 8, 0, 2], 'scores': [0.7102198251263578, 1.3488320996098073, 1.800310912953774, 2.0689115628861297, 2.2626643438740803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.15457284450531})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3996129035949707})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.4159443378448486})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.5330257415771484})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.5082533359527588})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.575911045074463})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.5505610704421997})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.6157469749450684})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8293, 'crossentropy': 1.3065974609375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0555410385131836})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9420217275619507})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0192210674285889})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9966021180152893})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9028311967849731})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 39830], ['id', 38256], ['id', 33593], ['id', 59732], ['id', 28152]], 'labels': [1, 2, 2, 2, 6], 'scores': [0.7757766526115493, 1.4223402668119305, 1.9163431392295829, 2.229314505643351, 2.445275478746288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.099808692932129})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.188572883605957})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2769240140914917})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.5219166278839111})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.311835527420044})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.485036849975586})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.6704411506652832})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.5438857078552246})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8367, 'crossentropy': 1.170812890625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.2038111686706543})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0776655673980713})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9320913553237915})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9852490425109863})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9266167879104614})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9676247835159302})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9424630403518677})
store['active_learning_steps'][9]['eval_training']['best_epoch']=7
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 46329], ['id', 14697], ['id', 16022], ['id', 49244], ['id', 37450]], 'labels': [3, 8, 8, 0, 4], 'scores': [0.8455998424400197, 1.5438400760922182, 2.075995994557206, 2.44275214214189, 2.6438421028484314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0610922574996948})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.305242896080017})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3827447891235352})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.651125192642212})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.47463858127594})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.3747122287750244})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.58864164352417})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.6578733921051025})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8362, 'crossentropy': 1.238059375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.931807279586792})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8547282814979553})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8546797037124634})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7777007818222046})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7841585874557495})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.805435836315155})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.791211724281311})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 49474], ['id', 828], ['id', 45917], ['id', 1929], ['id', 38133]], 'labels': [2, 4, 9, 5, 7], 'scores': [0.7622557528780353, 1.4481181582180191, 1.984997124834869, 2.326383671735803, 2.514865493453998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0132079124450684})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9939916729927063})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0912489891052246})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0529868602752686})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2485381364822388})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.1957650184631348})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.1229866743087769})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.133847713470459})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2781322002410889})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.2515645027160645})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.1350586414337158})
store['active_learning_steps'][11]['training']['best_epoch']=8
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.876, 'crossentropy': 1.00998408203125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1100094318389893})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9860552549362183})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9116499423980713})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8268221616744995})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.799278199672699})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9011664390563965})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.7740452289581299})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7792079448699951})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 8734], ['id', 5000], ['id', 32808], ['id', 37749], ['id', 7232]], 'labels': [5, 7, -1, 5, 5], 'scores': [0.880557914800223, 1.6050961096863492, 2.1860221532214448, 2.5984428790574245, 2.856312768847909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9527904391288757})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9201291799545288})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.036900281906128})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0611085891723633})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0987303256988525})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8652, 'crossentropy': 0.779747509765625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0864561796188354})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9004784822463989})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.8828489780426025})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8200244307518005})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 8958], ['id', 2000], ['id', 5315], ['id', 866], ['id', 3719]], 'labels': [3, 5, 3, 2, 2], 'scores': [0.7213360162010061, 1.3398507218597162, 1.8565332121670588, 2.261975243882457, 2.473531238914778]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9325830340385437})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9640121459960938})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9794403314590454})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.068597674369812})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.10231351852417})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.172797441482544})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1302211284637451})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1064178943634033})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.05413818359375})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2171411514282227})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1163777112960815})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.167441487312317})
store['active_learning_steps'][13]['training']['best_epoch']=9
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8596, 'crossentropy': 0.9856634765625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0237281322479248})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9446675181388855})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9533899426460266})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8679441213607788})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7928627729415894})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.805479884147644})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.872433066368103})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7461403012275696})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7674765586853027})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7523969411849976})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7862644195556641})
store['active_learning_steps'][13]['eval_training']['best_epoch']=8
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 39872], ['id', 1518], ['id', 58046], ['id', 30254], ['id', 12899]], 'labels': [8, 9, 8, 3, 8], 'scores': [0.9061343863151017, 1.6545993862998216, 2.234448102382345, 2.6429110036530026, 2.8948436898547474]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9437286853790283})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0128014087677002})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.147141456604004})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.014338731765747})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0588974952697754})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2261298894882202})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2481279373168945})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.1798722743988037})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8671, 'crossentropy': 0.9053734375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0372095108032227})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9861453771591187})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.8986393213272095})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.872779369354248})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8641191124916077})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8344240188598633})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.794092059135437})
store['active_learning_steps'][14]['eval_training']['best_epoch']=7
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 15855], ['id', 24795], ['id', 11054], ['id', 58560], ['id', 32254]], 'labels': [5, 4, 7, 0, 5], 'scores': [0.736904093381461, 1.359926237746739, 1.8437998619314304, 2.1969886530132516, 2.448515583685354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.1221061944961548})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9724738597869873})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.218985676765442})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1450709104537964})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.116087794303894})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2974038124084473})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0440837144851685})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2600960731506348})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.069582223892212})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.3635406494140625})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8612, 'crossentropy': 1.02543271484375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0768449306488037})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9095042943954468})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.8957912921905518})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8451945781707764})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8813464641571045})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 56191], ['id', 55472], ['id', 40589], ['id', 45326], ['id', 53560]], 'labels': [3, 3, 2, 8, -1], 'scores': [0.7737990767691743, 1.4822723898437768, 1.9744399805887793, 2.2964980928334517, 2.4830775674754406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9261078834533691})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0265922546386719})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9643117189407349})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0099297761917114})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0154216289520264})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.300595998764038})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1652477979660034})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.133910894393921})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8662, 'crossentropy': 0.9107744140625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.0342835187911987})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9052842855453491})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8538731336593628})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7719182968139648})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.719115138053894})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7684611678123474})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6741723418235779})
store['active_learning_steps'][16]['eval_training']['best_epoch']=7
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 24614], ['id', 15901], ['id', 27503], ['id', 24360], ['id', 6846]], 'labels': [5, 0, 2, 2, 2], 'scores': [0.8123858467196305, 1.4956789827182515, 2.0237001887990282, 2.4096835269240993, 2.6013553696269174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.009951114654541})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.933662474155426})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1263153553009033})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1626676321029663})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0604455471038818})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.350414752960205})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2395399808883667})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.3248560428619385})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8625, 'crossentropy': 1.0383517578125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.99001145362854})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7678936719894409})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7543176412582397})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.761045515537262})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7322711944580078})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7713425755500793})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.702734112739563})
store['active_learning_steps'][17]['eval_training']['best_epoch']=7
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 4488], ['id', 41027], ['id', 55531], ['id', 35694], ['id', 5452]], 'labels': [0, 0, 5, 9, 5], 'scores': [0.6811809814053107, 1.2584881886241157, 1.7586165416099968, 2.1301717516052197, 2.3753462489056973]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9673091173171997})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8541344404220581})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9259276986122131})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9755202531814575})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0478463172912598})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1618707180023193})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1770117282867432})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1868122816085815})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8785, 'crossentropy': 0.91718994140625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9609134197235107})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9461432695388794})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8206098675727844})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7932984232902527})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7604679465293884})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7333736419677734})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7317910194396973})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 667], ['id', 46570], ['id', 58626], ['id', 12385], ['id', 51371]], 'labels': [0, 3, 6, -1, 5], 'scores': [0.7227736887787695, 1.3676950872797682, 1.9041960154649602, 2.2362364986011407, 2.467935571772948]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.0885169506072998})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7935036420822144})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8477588891983032})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8454372882843018})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8761337399482727})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.061237096786499})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9220665097236633})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9324223399162292})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0971357822418213})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0272159576416016})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1383016109466553})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.882, 'crossentropy': 0.91574052734375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9850975871086121})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7925808429718018})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8164656162261963})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7647117376327515})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7147818803787231})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7224509119987488})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6486959457397461})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6912602186203003})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 16836], ['id', 43648], ['id', 18288], ['id', 8116], ['id', 3580]], 'labels': [7, 5, 8, 0, 5], 'scores': [0.6989434739268077, 1.286055846943018, 1.7764986539409495, 2.110497523192602, 2.3429252791776967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 0.9802919626235962})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.875144362449646})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8479341268539429})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9869661331176758})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9324193000793457})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9267544746398926})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0424118041992188})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0073601007461548})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0603941679000854})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.875, 'crossentropy': 0.88510517578125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8698681592941284})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.6532580256462097})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6596713066101074})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6160916090011597})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6212674975395203})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6022881269454956})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5873597860336304})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.5989148616790771})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 7726], ['id', 22375], ['id', 31599], ['id', 9633], ['id', 187]], 'labels': [4, -1, -1, 9, 2], 'scores': [0.6651768596930614, 1.280110284458578, 1.7670066227621168, 2.110824576778886, 2.3429227745516252]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.0484174489974976})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8197879195213318})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.836051881313324})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8696704506874084})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9071764945983887})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9745873212814331})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8751, 'crossentropy': 0.761323095703125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0122780799865723})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7736648321151733})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7412698268890381})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6761512756347656})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6394593715667725})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 10210], ['id', 34899], ['id', 30454], ['id', 8443], ['id', 26892]], 'labels': [3, 7, 6, 2, -1], 'scores': [0.7095803074138718, 1.3358540869669966, 1.849981762734858, 2.2179471673669306, 2.4346689063968796]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9870742559432983})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8021771311759949})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.967553973197937})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8874384164810181})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8574240803718567})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0345656871795654})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1182427406311035})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8796, 'crossentropy': 0.77555732421875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9105392694473267})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7614660859107971})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.6718806028366089})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6392475366592407})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.620133638381958})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.607463538646698})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 1311], ['id', 30889], ['id', 2151], ['id', 30130], ['id', 50371]], 'labels': [5, 2, -1, 3, 7], 'scores': [0.6006355340484211, 1.1102291411535847, 1.5345352119305637, 1.8696186327523652, 2.0602347881460785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9538270235061646})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7746934294700623})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8392475843429565})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8396096229553223})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9484597444534302})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0466737747192383})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8711, 'crossentropy': 0.790515234375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9490503072738647})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7020622491836548})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6629889011383057})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6551847457885742})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6162763833999634})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 57221], ['id', 4058], ['id', 22210], ['id', 36515], ['id', 45094]], 'labels': [-1, 8, -1, 3, 2], 'scores': [0.6872941937122101, 1.2685714261412517, 1.748772060776293, 2.082869576107357, 2.3349678570578734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0673625469207764})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9127625226974487})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9289606809616089})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9853741526603699})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.059454321861267})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9690163731575012})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0811725854873657})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.2197668552398682})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9546733498573303})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.06300950050354})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0516273975372314})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 1.1003336906433105})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.144134521484375})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.3133598566055298})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.3211829662322998})
store['active_learning_steps'][24]['training']['best_epoch']=12
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.878, 'crossentropy': 1.09983017578125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9946295022964478})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.712854266166687})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7425544261932373})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7032804489135742})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7806936502456665})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7115504741668701})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 4887], ['id', 4611], ['id', 3382], ['id', 50042], ['id', 36238]], 'labels': [8, -1, 9, -1, 7], 'scores': [0.8060205525825805, 1.5452786292015, 2.126253724360114, 2.504394194313799, 2.7616894441210613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.147156000137329})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.899929404258728})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0547994375228882})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9241898059844971})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0061497688293457})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9575870037078857})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0202574729919434})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1293435096740723})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.084644079208374})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0651652812957764})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9779419898986816})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1169581413269043})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1683039665222168})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1166152954101562})
store['active_learning_steps'][25]['training']['best_epoch']=11
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8854, 'crossentropy': 0.96522587890625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0373423099517822})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7711399793624878})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9158737659454346})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8299275636672974})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8381925225257874})
store['active_learning_steps'][25]['eval_training']['best_epoch']=2
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 33802], ['id', 12513], ['id', 33055], ['id', 10256], ['id', 39662]], 'labels': [-1, 8, 6, 2, 8], 'scores': [0.7969457824628607, 1.4983896099059955, 2.056027030328825, 2.3914990266039036, 2.6034702393380433]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.1232566833496094})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8616901636123657})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8989945650100708})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8840878009796143})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.040414571762085})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0374072790145874})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.067077875137329})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0896692276000977})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0201716423034668})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9066861867904663})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0237524509429932})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9619518518447876})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9577374458312988})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 1.0324690341949463})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.475377082824707})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2725062370300293})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9712346196174622})
store['active_learning_steps'][26]['training']['best_epoch']=14
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8868, 'crossentropy': 1.02725634765625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.1555497646331787})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8659362196922302})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8806596994400024})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7657296061515808})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8638359308242798})
store['active_learning_steps'][26]['eval_training']['best_epoch']=2
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 47090], ['id', 18904], ['id', 10580], ['id', 55778], ['id', 12151]], 'labels': [-1, 6, -1, -1, 3], 'scores': [0.8259508405795919, 1.5638141111583992, 2.1032444839386093, 2.4366159506736, 2.6265071357882217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.140167236328125})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9249181747436523})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7995395660400391})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9919554591178894})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9961819052696228})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9766553640365601})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.88, 'crossentropy': 0.734858740234375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0472519397735596})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8194279670715332})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6781102418899536})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6753432750701904})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.6498050689697266})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 12497], ['id', 2831], ['id', 52708], ['id', 8646], ['id', 46619]], 'labels': [0, 1, 4, 5, -1], 'scores': [0.6585299255213357, 1.2252966390738491, 1.6863171465434226, 2.008537675311927, 2.223372703053193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.008122205734253})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.728894054889679})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6936517953872681})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.809285044670105})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7507095336914062})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7922778725624084})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8625634908676147})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8381820917129517})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8496013879776001})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8982, 'crossentropy': 0.718422265625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9476936459541321})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6728601455688477})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6024219989776611})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6310887336730957})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5873632431030273})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5578488111495972})
store['active_learning_steps'][28]['eval_training']['best_epoch']=3
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 58258], ['id', 6818], ['id', 52644], ['id', 17813], ['id', 54278]], 'labels': [7, -1, 7, 7, 7], 'scores': [0.76703370530123, 1.3395461849216992, 1.7522219768295653, 2.0802505172241843, 2.33818728529803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.0275044441223145})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6955797672271729})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7255780100822449})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7425069808959961})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7798261642456055})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7101040482521057})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8434576988220215})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.051804780960083})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8685644268989563})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9042, 'crossentropy': 0.66996640625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9193451404571533})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6126500368118286})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5247367024421692})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5511451959609985})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5053893327713013})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4834287166595459})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5206218361854553})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4821004867553711})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 40066], ['id', 39130], ['id', 32856], ['id', 2595], ['id', 24424]], 'labels': [4, 6, 2, 9, 1], 'scores': [0.6568730545726889, 1.2403558523813722, 1.6985705571428573, 2.026746008073623, 2.221605500007315]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.95225989818573})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7158461213111877})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6075445413589478})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7422157526016235})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.73409104347229})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6579403877258301})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.56158935546875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9380916953086853})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6557771563529968})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5803692936897278})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.548696756362915})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5227693319320679})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 13156], ['id', 9608], ['id', 24982], ['id', 40136], ['id', 54802]], 'labels': [2, 8, 2, 9, 6], 'scores': [0.6753247525090755, 1.2736167499149644, 1.7505017246951047, 2.0856554576832194, 2.315084225692808]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.9707489013671875})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.653255820274353})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6574810147285461})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6774561405181885})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7516579627990723})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8952, 'crossentropy': 0.5992294921875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.925801157951355})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7046307325363159})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6187320351600647})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5958881378173828})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 49202], ['id', 45424], ['id', 28371], ['id', 7833], ['id', 49472]], 'labels': [5, 4, 3, 5, -1], 'scores': [0.6339830253922554, 1.168981104138573, 1.5967096137487262, 1.9304883386445253, 2.1643035904697214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.017073392868042})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7040643692016602})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6576839685440063})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6824303269386292})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7733209729194641})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7101801633834839})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7280902862548828})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7546401619911194})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7077254056930542})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8216456174850464})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8320238590240479})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8102242946624756})
store['active_learning_steps'][32]['training']['best_epoch']=9
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9094, 'crossentropy': 0.704124462890625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0407228469848633})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6192005276679993})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5366373658180237})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5335096120834351})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5692201852798462})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5354529619216919})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4835376441478729})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.48684096336364746})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.46704310178756714})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.46803146600723267})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4704744815826416})
store['active_learning_steps'][32]['eval_training']['best_epoch']=8
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 2793], ['id', 51000], ['id', 134], ['id', 37489], ['id', 54612]], 'labels': [9, -1, 1, 2, 8], 'scores': [0.6901705591601992, 1.3345035046274076, 1.8307366995371228, 2.194637150448374, 2.4528444149449733]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9807767868041992})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6323765516281128})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6974313259124756})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6770728826522827})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9424811601638794})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.57776416015625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.0777587890625})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6793632507324219})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6568905115127563})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5873153209686279})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 6291], ['id', 29591], ['id', 26733], ['id', 16676], ['id', 45982]], 'labels': [3, 9, 2, 3, 4], 'scores': [0.6237004627298988, 1.1476703971576292, 1.5950308054396904, 1.9447860408447006, 2.19065064710475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0541377067565918})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6459028124809265})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.577912449836731})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6930339336395264})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.726048469543457})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7321445345878601})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9168, 'crossentropy': 0.540147216796875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9121724367141724})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6860736608505249})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6157070398330688})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5636008977890015})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5554780960083008})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 46126], ['id', 24632], ['id', 44948], ['id', 5787], ['id', 16961]], 'labels': [3, 2, 9, 3, 0], 'scores': [0.6494985241496769, 1.1760804014641706, 1.6324647043492782, 1.9801472997996976, 2.2117317911504513]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9960556030273438})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6208533048629761})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5769540071487427})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6474584341049194})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6038765907287598})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6321009397506714})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6353381276130676})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7413908243179321})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6419960856437683})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7018342018127441})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.639026403427124})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7472400665283203})
store['active_learning_steps'][35]['training']['best_epoch']=9
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9186, 'crossentropy': 0.62930703125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.9631283283233643})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6227810978889465})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5595464706420898})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5050170421600342})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5023103952407837})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.44799405336380005})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4539835453033447})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.44093912839889526})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.43083053827285767})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 17467], ['id', 38549], ['id', 491], ['id', 51154], ['id', 10338]], 'labels': [3, 3, -1, 3, 4], 'scores': [0.7553944011292474, 1.4266600956626565, 1.9179431182009363, 2.2589802403047923, 2.453277194804577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.0943882465362549})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6996009349822998})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6141223907470703})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6473135948181152})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5615420341491699})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5812147259712219})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6030629873275757})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6968053579330444})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.683308482170105})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.56582958984375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.003132939338684})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6072322130203247})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.525425910949707})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5204393267631531})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4633939862251282})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4480857849121094})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4625224173069})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.42295318841934204})
store['active_learning_steps'][36]['eval_training']['best_epoch']=8
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 23104], ['id', 42656], ['id', 34328], ['id', 46175], ['id', 34815]], 'labels': [0, 8, 8, 8, 3], 'scores': [0.8488754750648282, 1.434338912129491, 1.9039405385631527, 2.2262559443120944, 2.425493945300686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.0568914413452148})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5980631709098816})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5425231456756592})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5516092777252197})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5187355875968933})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5883829593658447})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9276, 'crossentropy': 0.4774662109375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.051662564277649})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6002821326255798})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5403294563293457})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5518473386764526})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4971212148666382})
store['active_learning_steps'][37]['eval_training']['best_epoch']=5
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 17958], ['id', 44095], ['id', 14749], ['id', 51759], ['id', 16485]], 'labels': [9, 2, 0, 3, -1], 'scores': [0.5944136101815012, 1.1464398516703649, 1.6098209408477828, 1.9498786710966884, 2.1753669718181694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.0993340015411377})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6940139532089233})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6170220375061035})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6121495366096497})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5675685405731201})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.603995680809021})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6518867611885071})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6440593004226685})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9273, 'crossentropy': 0.527921875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.956792950630188})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6017926931381226})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5561155080795288})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4563578963279724})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4759906530380249})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.45854753255844116})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.43695998191833496})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 670], ['id', 59447], ['id', 24613], ['id', 12254], ['id', 41772]], 'labels': [3, 8, 9, 2, 5], 'scores': [0.6389677987030704, 1.208851983472202, 1.6916508368089875, 2.0485808462305863, 2.3000914485746016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0800540447235107})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5928988456726074})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5632697343826294})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5886647701263428})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5712178945541382})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5900239944458008})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5980439186096191})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5794117450714111})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6398611664772034})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6255220174789429})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6950907707214355})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6025316119194031})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6115723252296448})
store['active_learning_steps'][39]['training']['best_epoch']=10
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9356, 'crossentropy': 0.568712646484375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0312106609344482})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6037949919700623})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5799756050109863})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.48940128087997437})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5005019307136536})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.4793239235877991})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.46230050921440125})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4204629063606262})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.412337064743042})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.41791877150535583})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.39465951919555664})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.41983336210250854})
store['active_learning_steps'][39]['eval_training']['best_epoch']=9
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 42793], ['id', 24547], ['id', 45018], ['id', 3457], ['id', 9558]], 'labels': [4, 4, -1, -1, 4], 'scores': [0.8100214419567616, 1.4680267470234472, 1.9977039208877518, 2.354885213623062, 2.567299886767933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.175113320350647})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6109055280685425})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5881065130233765})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5721452236175537})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.592507004737854})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6329320669174194})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5675950050354004})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.65887451171875})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9249, 'crossentropy': 0.52162685546875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.0781450271606445})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.638610303401947})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4697860777378082})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.47411054372787476})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5053113698959351})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.45479869842529297})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.44111698865890503})
store['active_learning_steps'][40]['eval_training']['best_epoch']=6
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 31014], ['id', 12984], ['id', 2761], ['id', 25564], ['id', 13677]], 'labels': [8, 8, 8, -1, 8], 'scores': [0.7364606686234882, 1.3354959693654478, 1.8100659441601703, 2.1523828930892925, 2.3782668909758575]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.1587378978729248})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7452424764633179})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.589333176612854})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5051274299621582})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.603197455406189})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5585691928863525})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5206079483032227})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9283, 'crossentropy': 0.510485595703125}
