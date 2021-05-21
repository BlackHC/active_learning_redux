store = {}
store['timestamp']=1621483133
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=73']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=73
store['worker_id']=73
store['num_workers']=80
store['config']={'seed': 1311, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.280320644378662})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.1875991821289062})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.710622549057007})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.0059242248535156})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 3.746479034423828})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 3.9473495483398438})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 4.156055927276611})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.591, 'crossentropy': 3.425179296875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 16786], ['id', 28501], ['id', 24014], ['id', 20314], ['id', 47663]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.4801049810568885, 2.622979035406188, 3.4570466835292137, 3.9937245451123236, 4.309445164770422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5849609375, 'crossentropy': 1.6411688327789307})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.229437828063965})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.803586483001709})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.959921360015869})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.8874192237854004})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.9197030067443848})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.6868419647216797})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.7381367683410645})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5957, 'crossentropy': 2.9734146484375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 44299], ['id', 25316], ['id', 38156], ['id', 36752], ['id', 27247]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.1205559659223816, 2.0598996893948263, 2.859465057040027, 3.4359114402629984, 3.8276427834113473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.5498883724212646})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.048067569732666})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.4474682807922363})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.415696144104004})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.3697664737701416})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.6889543533325195})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.906423568725586})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5985, 'crossentropy': 2.487905859375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 39750], ['id', 42826], ['id', 19132], ['id', 26254], ['id', 43112]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9682848290450021, 1.742443424990439, 2.4287714168603696, 2.9917699760304934, 3.418472526473094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.6532831192016602})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.9021649360656738})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.4823546409606934})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.4966189861297607})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7328968048095703})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.984642505645752})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.975733757019043})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.1722240447998047})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.7292065620422363})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.753462791442871})
store['active_learning_steps'][3]['training']['best_epoch']=7
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5932, 'crossentropy': 3.1829583984375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 17170], ['id', 20982], ['id', 20330], ['id', 21346], ['id', 9771]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9734105817859418, 1.8622324414427665, 2.658866451752681, 3.241787079915402, 3.7086422457249464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.422855257987976})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.1074728965759277})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.1720917224884033})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.1353750228881836})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.2092580795288086})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.4930944442749023})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5865097045898438})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.541482448577881})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.474156141281128})
store['active_learning_steps'][4]['training']['best_epoch']=6
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6101, 'crossentropy': 2.6296173828125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 59771], ['id', 2731], ['id', 7584], ['id', 33276], ['id', 29007]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1151721390266074, 1.9661771601716223, 2.71413054827362, 3.305919100673849, 3.713658954847741]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.377663016319275})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.855311632156372})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.0772218704223633})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.193197727203369})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5089468955993652})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.552708625793457})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.5804433822631836})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.601775646209717})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.768502712249756})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.9374542236328125})
store['active_learning_steps'][5]['training']['best_epoch']=7
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6131, 'crossentropy': 2.6865259765625}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 23586], ['id', 31557], ['id', 21901], ['id', 62], ['id', 23680]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9961128014386627, 1.8977583983065553, 2.703450486249208, 3.3123152350727114, 3.760755367196058]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.329358458518982})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.7440944910049438})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.8602204322814941})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.9744806289672852})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.197216033935547})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6342, 'crossentropy': 1.7187986328125}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 11992], ['id', 3947], ['id', 40168], ['id', 13195], ['id', 41329]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7591661737865611, 1.4311567630991178, 2.037312442856945, 2.5751659071324102, 3.019986077804088]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.3264751434326172})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.8898212909698486})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.1562647819519043})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.4417357444763184})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.3723130226135254})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.232722043991089})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.4958558082580566})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.9128427505493164})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.5101711750030518})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.770176410675049})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7297921180725098})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.740685224533081})
store['active_learning_steps'][7]['training']['best_epoch']=9
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6221, 'crossentropy': 2.93616875}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 34634], ['id', 52580], ['id', 1799], ['id', 33801], ['id', 29754]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0310458259034518, 1.9109853651169617, 2.680347218494946, 3.316008670646532, 3.773732823713182]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.3222942352294922})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5831108093261719})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.8446853160858154})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.0206122398376465})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.220395088195801})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.1699955463409424})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.3274502754211426})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.3400187492370605})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.3097167015075684})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.3446884155273438})
store['active_learning_steps'][8]['training']['best_epoch']=7
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6151, 'crossentropy': 2.6299216796875}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 6844], ['id', 448], ['id', 7383], ['id', 44278], ['id', 31587]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.2093142399741303, 2.123814889904791, 2.8863776475314378, 3.4901618674681814, 3.888764766744245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.4686083793640137})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5720982551574707})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.0710482597351074})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.0064432621002197})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.104390859603882})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.442216634750366})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.7676358222961426})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4095592498779297})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6238, 'crossentropy': 2.2126203125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 31065], ['id', 54813], ['id', 34303], ['id', 25963], ['id', 1254]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9455634039371437, 1.7564340864060002, 2.4636932348360894, 3.080389701445318, 3.5596023294759327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.3856678009033203})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.5582475662231445})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.995615005493164})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.342832565307617})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.397036075592041})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.3315060138702393})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.5942320823669434})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.4290807247161865})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.4729514122009277})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.843197822570801})
store['active_learning_steps'][10]['training']['best_epoch']=7
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6234, 'crossentropy': 2.84709765625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 55016], ['id', 32046], ['id', 45908], ['id', 27863], ['id', 19478]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9399843420431577, 1.7946078924382536, 2.5587648956395466, 3.202438529015687, 3.6742962298523096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.3664822578430176})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.5269598960876465})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.957930326461792})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.072490692138672})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.3538546562194824})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.4486358165740967})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.335428237915039})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.699634075164795})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6184, 'crossentropy': 2.417821875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 45096], ['id', 44011], ['id', 1031], ['id', 46375], ['id', 58451]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9306476373242953, 1.7660155952490824, 2.4587541151012324, 3.038396943473174, 3.490290014551885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.316022276878357})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.4399347305297852})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.7303452491760254})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.8869059085845947})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.002622127532959})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.99858558177948})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.0793232917785645})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.2588248252868652})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.101998805999756})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.534897804260254})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.0056896209716797})
store['active_learning_steps'][12]['training']['best_epoch']=8
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6653, 'crossentropy': 2.387221484375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 13598], ['id', 46609], ['id', 54405], ['id', 33854], ['id', 4436]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.8810512985790764, 1.7278059769183005, 2.5008051604840755, 3.136012346631695, 3.597068343994673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.5478515625, 'crossentropy': 1.4244933128356934})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.312056541442871})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.6238596439361572})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.957452416419983})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.1423325538635254})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.297105550765991})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6180315017700195})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.635, 'crossentropy': 1.943289453125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 1473], ['id', 33141], ['id', 49891], ['id', 3906], ['id', 50045]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8424786365576948, 1.5707211140569486, 2.2114820681433427, 2.7629555861620556, 3.226724461462263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.552734375, 'crossentropy': 1.3732542991638184})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2905848026275635})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.445963978767395})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.5728857517242432})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.6028094291687012})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.8375040292739868})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.946552038192749})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.0373334884643555})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.872615098953247})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.927886962890625})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.121650457382202})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.1797027587890625})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.1995773315429688})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.5908377170562744})
store['active_learning_steps'][14]['training']['best_epoch']=11
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6479, 'crossentropy': 2.5066875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 43428], ['id', 25434], ['id', 56769], ['id', 3806], ['id', 30247]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0561905785576187, 1.9701774807961652, 2.7110474549078614, 3.3237968338104658, 3.772838425226853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.546875, 'crossentropy': 1.3797638416290283})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3282909393310547})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.4779479503631592})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.5341291427612305})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.520148754119873})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.919323444366455})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.7876869440078735})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.8582749366760254})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.8732235431671143})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.113973617553711})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.666, 'crossentropy': 2.055470703125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 24815], ['id', 26966], ['id', 7593], ['id', 57927], ['id', 35052]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.906754350533653, 1.7491166981590833, 2.5054440121612114, 3.122607966093879, 3.6064945165291444]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.560546875, 'crossentropy': 1.3699009418487549})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2404720783233643})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.3325564861297607})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.5261938571929932})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7734942436218262})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.0128090381622314})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.012160539627075})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.006390333175659})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.198148012161255})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.326430320739746})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.1627330780029297})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.2744646072387695})
store['active_learning_steps'][16]['training']['best_epoch']=9
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6646, 'crossentropy': 2.2199798828125}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 39688], ['id', 37251], ['id', 43277], ['id', 48763], ['id', 7609]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9820882627850613, 1.8805861363203622, 2.6198353081845083, 3.2401290623385917, 3.6760160053485116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.541015625, 'crossentropy': 1.4263842105865479})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2543715238571167})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.4089374542236328})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.427555799484253})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.750009298324585})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.7064659595489502})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.876794457435608})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.919713020324707})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6583, 'crossentropy': 1.7799978515625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 43529], ['id', 15248], ['id', 56561], ['id', 57290], ['id', 530]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8372719472065169, 1.5980335997369761, 2.304035475019739, 2.8753080339107004, 3.3312545558717463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.2937467098236084})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.2256433963775635})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.350621223449707})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.4933533668518066})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.5596826076507568})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6255265474319458})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.910454273223877})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.643, 'crossentropy': 1.61738779296875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 38772], ['id', 39685], ['id', 6311], ['id', 26462], ['id', 30405]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.8196268037235868, 1.582178639551822, 2.2400695976191756, 2.815384018665018, 3.270544882664953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5732421875, 'crossentropy': 1.3345403671264648})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1491742134094238})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2803623676300049})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.6564393043518066})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.3717652559280396})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.6323919296264648})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.6601576805114746})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.7331873178482056})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.7377686500549316})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6765, 'crossentropy': 1.6539890625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 33405], ['id', 35309], ['id', 52223], ['id', 70], ['id', 17989]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8445947079660914, 1.6356821785319453, 2.352597664210924, 2.9629205082511625, 3.431561435358402]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.5078125, 'crossentropy': 1.4735525846481323})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.2325468063354492})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2729524374008179})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.3442152738571167})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.4323557615280151})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.6278798580169678})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.7804338932037354})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6635, 'crossentropy': 1.43738037109375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 34744], ['id', 18098], ['id', 7242], ['id', 15738], ['id', 17987]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8672583144165498, 1.6941399648549242, 2.3619120857192906, 2.894249337306955, 3.3139609035980477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5458984375, 'crossentropy': 1.4085659980773926})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2429691553115845})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2780003547668457})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.3975567817687988})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.4843673706054688})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.5693680047988892})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.623117208480835})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.677627444267273})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.724029541015625})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.938791275024414})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.811760425567627})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.8334228992462158})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.772293210029602})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.6670098304748535})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.0464746952056885})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.9234901666641235})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.985058307647705})
store['active_learning_steps'][21]['training']['best_epoch']=14
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6893, 'crossentropy': 1.8668484375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 31612], ['id', 16490], ['id', 29088], ['id', 36117], ['id', 39483]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.101235917631153, 2.0371890530318737, 2.827688393775559, 3.427593146658147, 3.8522398327687366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.52734375, 'crossentropy': 1.44862961769104})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.1661009788513184})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.22169828414917})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.3771412372589111})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.3453254699707031})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.578279733657837})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.7066984176635742})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6699, 'crossentropy': 1.4571162109375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 21960], ['id', 55037], ['id', 36120], ['id', 40732], ['id', 21381]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.718791555066439, 1.4012472956349966, 2.0113746620111543, 2.5518650937761542, 3.0151036900224817]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.4109909534454346})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1943086385726929})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1819881200790405})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.3081635236740112})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.3329086303710938})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.471265196800232})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.50669264793396})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.614138126373291})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6559644937515259})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.7199140787124634})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.86396062374115})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.7132887840270996})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9189043045043945})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8875048160552979})
store['active_learning_steps'][23]['training']['best_epoch']=11
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6799, 'crossentropy': 1.9444830078125}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 11901], ['id', 42917], ['id', 48441], ['id', 39951], ['id', 4809]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.0467554897393647, 1.9934238695669038, 2.7666308849344796, 3.3781759730915937, 3.803539762290563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.5341796875, 'crossentropy': 1.5351648330688477})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.2438628673553467})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.2061357498168945})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.37431001663208})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.3549222946166992})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.4279836416244507})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.5901553630828857})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.5685569047927856})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.596564769744873})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.784245491027832})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.7155303955078125})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.8907612562179565})
store['active_learning_steps'][24]['training']['best_epoch']=9
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6874, 'crossentropy': 1.7561943359375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 58420], ['id', 36424], ['id', 20038], ['id', 41355], ['id', 168]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9201149860842599, 1.7716486900350095, 2.49789136931508, 3.105135168117318, 3.561040515220628]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5380859375, 'crossentropy': 1.5818166732788086})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.2243385314941406})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2794218063354492})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.3766440153121948})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.481136679649353})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4477518796920776})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.5266497135162354})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.7569983005523682})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.672387719154358})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6156911849975586})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.8491795063018799})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.7009773254394531})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.624391794204712})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.0469918251037598})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.8240413665771484})
store['active_learning_steps'][25]['training']['best_epoch']=12
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6777, 'crossentropy': 1.8513130859375}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 20302], ['id', 5413], ['id', 48019], ['id', 15405], ['id', 5918]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0272228937562016, 1.97581612011167, 2.7555284663293023, 3.352518141476887, 3.7999214666432337]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.49609375, 'crossentropy': 1.6611206531524658})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.177790641784668})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1694071292877197})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.3083500862121582})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.4444606304168701})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3884761333465576})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4163188934326172})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.588193416595459})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.7162988185882568})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7188966274261475})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6812, 'crossentropy': 1.5915181640625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 21864], ['id', 9692], ['id', 17654], ['id', 59091], ['id', 31827]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8188615776911032, 1.5951546742180693, 2.292254566248154, 2.86964292871971, 3.3489414585397803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.451171875, 'crossentropy': 1.6291687488555908})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1646971702575684})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1882331371307373})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3470391035079956})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.4220657348632812})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.3140146732330322})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3896732330322266})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4737778902053833})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.5294562578201294})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6915, 'crossentropy': 1.4844310546875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 50529], ['id', 1087], ['id', 3895], ['id', 21929], ['id', 38782]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8058639232996883, 1.5457035921810238, 2.1696841416712953, 2.7216181943084763, 3.172608003504836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.5361328125, 'crossentropy': 1.4653162956237793})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.253951072692871})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3191416263580322})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3306798934936523})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3479175567626953})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.4987709522247314})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.5089534521102905})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7725112438201904})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.8991413116455078})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7207140922546387})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.5713903903961182})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.9411636590957642})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.7882585525512695})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.9654746055603027})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.9850246906280518})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.8892507553100586})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.7617135047912598})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.0067319869995117})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.975624918937683})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.897740125656128})
store['active_learning_steps'][28]['training']['best_epoch']=17
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7, 'crossentropy': 1.8747365234375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 42603], ['id', 32351], ['id', 18530], ['id', 14463], ['id', 45967]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0521680147909076, 2.007106187856034, 2.802316380061564, 3.415739584998563, 3.857760729362064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.458984375, 'crossentropy': 1.657862901687622})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.3146274089813232})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2485237121582031})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.298753261566162})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.4765770435333252})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.4866881370544434})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.480692982673645})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.8052815198898315})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.896536111831665})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6813, 'crossentropy': 1.71305234375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 587], ['id', 44492], ['id', 57174], ['id', 39997], ['id', 57792]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8146281664893524, 1.5324944637927445, 2.16740728767667, 2.7270543303406907, 3.1960678554174136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.5302734375, 'crossentropy': 1.563974380493164})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.1857564449310303})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1974228620529175})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2160842418670654})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.3438215255737305})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3198792934417725})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4605538845062256})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.496168613433838})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.6351470947265625})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.7548308372497559})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.8279526233673096})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.6606090068817139})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.7011632919311523})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.8288660049438477})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.6859533786773682})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.797196388244629})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.8095046281814575})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.7850849628448486})
store['active_learning_steps'][30]['training']['best_epoch']=15
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6923, 'crossentropy': 1.82323515625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 26300], ['id', 23569], ['id', 3694], ['id', 20173], ['id', 22547]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9609520622704664, 1.8418241148756849, 2.594831395865076, 3.221617839739225, 3.705430442167885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.4853515625, 'crossentropy': 1.547963261604309})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2612391710281372})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2419590950012207})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3895751237869263})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.4370696544647217})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.6408727169036865})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.6538074016571045})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.7730772495269775})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.0025134086608887})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.9388132095336914})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6581, 'crossentropy': 1.7751091796875}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 55018], ['id', 17030], ['id', 34408], ['id', 42199], ['id', 36388]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8675291588387559, 1.6271173890122728, 2.2973714476835028, 2.872876341390695, 3.3383448612699667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.5029296875, 'crossentropy': 1.6117171049118042})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1844922304153442})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2239508628845215})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1932587623596191})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3433778285980225})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.3880151510238647})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.4039236307144165})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.4482969045639038})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.746965765953064})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.7087777853012085})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.601865291595459})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7026, 'crossentropy': 1.60533076171875}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 51860], ['id', 6000], ['id', 55968], ['id', 51402], ['id', 12078]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8458800886826614, 1.6344829172034743, 2.3674545792114277, 2.962554036516071, 3.426166675307625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.5078125, 'crossentropy': 1.5170875787734985})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.2841159105300903})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2021092176437378})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2261784076690674})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2271071672439575})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.418125867843628})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.4794056415557861})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.628592610359192})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7819820642471313})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.6928867101669312})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.7984524965286255})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.9950920343399048})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6647, 'crossentropy': 1.9041904296875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 5643], ['id', 11624], ['id', 36400], ['id', 15622], ['id', 41358]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8505332284231086, 1.6286150013441505, 2.338997499679872, 2.944980832864556, 3.4111572079343606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.4912109375, 'crossentropy': 1.631112813949585})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.3353182077407837})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.250259280204773})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.4073822498321533})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2989753484725952})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.4240834712982178})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4791314601898193})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.8132984638214111})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.8114516735076904})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.81422758102417})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.8445234298706055})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.7563772201538086})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.8863520622253418})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.0786190032958984})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.125397205352783})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.0530312061309814})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.225558042526245})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.329023838043213})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.2529497146606445})
store['active_learning_steps'][34]['training']['best_epoch']=16
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.692, 'crossentropy': 2.2299822265625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 5893], ['id', 13903], ['id', 59264], ['id', 46796], ['id', 16676]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0699947978774687, 1.9988754097701116, 2.814685894561528, 3.408356609615206, 3.837993714496264]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.435546875, 'crossentropy': 1.7189369201660156})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1954474449157715})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1651840209960938})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.306380033493042})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2880394458770752})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.5998860597610474})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5462522506713867})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.5713152885437012})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.8170424699783325})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.7699778079986572})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6766, 'crossentropy': 1.6535724609375}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 11016], ['id', 31256], ['id', 12461], ['id', 56244], ['id', 44676]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8260951307070143, 1.6058651081929676, 2.2800487570204098, 2.8276410009875512, 3.2714088579781144]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.5078125, 'crossentropy': 1.536998987197876})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.2627310752868652})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1642870903015137})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2936434745788574})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2789891958236694})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.390963077545166})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.6271300315856934})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5014441013336182})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.6378648281097412})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.7967963218688965})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.946642279624939})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.8301159143447876})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6947, 'crossentropy': 1.7977166015625}
