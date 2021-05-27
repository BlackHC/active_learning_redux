store = {}
store['timestamp']=1622124551
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=35']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=35
store['worker_id']=35
store['num_workers']=80
store['config']={'seed': 1271, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.2919068336486816})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.795592784881592})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.0467305183410645})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.4780008792877197})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.456738233566284})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.5525217056274414})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.4642019271850586})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.5758817195892334})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.9617252349853516})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.6642887592315674})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.5899763107299805})
store['active_learning_steps'][0]['training']['best_epoch']=8
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5987, 'crossentropy': 3.88392265625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.9284417629241943})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 1.7978150844573975})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.1176271438598633})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.175797462463379})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.108506202697754})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 14991], ['ood', 40152], ['ood', 51625], ['id', 8861], ['id', 35427]], 'labels': [-1, -1, -1, 4, 6], 'scores': [1.1586993821763363, 2.003321461625995, 2.575460253438419, 2.9735601197586616, 3.2080866938676933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.9741888046264648})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.4732131958007812})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.166367292404175})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.099931240081787})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.642739772796631})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.525738000869751})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.543654680252075})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.57918119430542})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5968, 'crossentropy': 3.49571328125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.7243281602859497})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.7222861051559448})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.8038603067398071})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.9289429187774658})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 50558], ['ood', 28860], ['ood', 9633], ['ood', 46565], ['ood', 45201]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1182881933771625, 1.766511348183269, 2.260537299938223, 2.6254461153439075, 2.842850798727738]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 2.2958531379699707})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.905604124069214})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.0209436416625977})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.13529372215271})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 3.4416637420654297})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.5505199432373047})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.5876, 'crossentropy': 3.379126953125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.8158106803894043})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.7842752933502197})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.849539041519165})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 1.72886061668396})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.7516603469848633})
store['active_learning_steps'][2]['eval_training']['best_epoch']=5
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 30380], ['ood', 20631], ['ood', 59468], ['ood', 32218], ['ood', 4797]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0113222871004932, 1.7678464605817998, 2.4012483180820543, 2.8280031655042785, 3.074725420807748]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5751953125, 'crossentropy': 2.3240206241607666})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 2.907708168029785})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.920177459716797})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.3189196586608887})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 3.455413341522217})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.7133045196533203})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.5872, 'crossentropy': 3.2049677734375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.517366647720337})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.680664300918579})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 1.6197724342346191})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 1.618501901626587})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.6341408491134644})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['ood', 28632], ['ood', 6313], ['ood', 46908], ['ood', 7367], ['ood', 56503]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9655296359113938, 1.8207524013756229, 2.469447465008535, 2.875709675324116, 3.07522909038268]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.2549946308135986})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.781700372695923})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.8833725452423096})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.3455910682678223})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.530205249786377})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5866, 'crossentropy': 2.892367578125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.6030621528625488})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.588172435760498})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.4846192598342896})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.5136384963989258})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 14286], ['id', 49518], ['ood', 26162], ['ood', 28359], ['ood', 36197]], 'labels': [-1, 5, -1, -1, -1], 'scores': [0.9787178371542051, 1.7534663045355943, 2.427269635072637, 2.75363534560238, 2.9384922858237243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 2.024420976638794})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.32755708694458})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.5053563117980957})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.6638941764831543})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.978394031524658})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.025252342224121})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.4435224533081055})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.193333625793457})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6128, 'crossentropy': 3.140150390625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.7933272123336792})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.8682769536972046})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.776373028755188})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 1.763297438621521})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.7682271003723145})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 1.8566384315490723})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 37019], ['ood', 59148], ['ood', 48018], ['ood', 54933], ['id', 49798]], 'labels': [-1, -1, -1, -1, 1], 'scores': [1.0203364706322686, 1.7201372069973964, 2.3021341270575624, 2.704948965397124, 2.901842522146531]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.8045029640197754})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.47910475730896})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.427811861038208})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6874399185180664})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.7867183685302734})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.9697608947753906})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.77079439163208})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6282, 'crossentropy': 2.6227345703125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.5870801210403442})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.5463876724243164})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.4843814373016357})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.5022543668746948})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.534294605255127})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.4358630180358887})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 12396], ['ood', 48111], ['id', 3712], ['id', 10754], ['id', 4572]], 'labels': [-1, -1, 3, 8, 7], 'scores': [0.8965771711436419, 1.561863824763577, 2.0915305589311783, 2.492854417680794, 2.786694711949231]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.9176573753356934})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.2720794677734375})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.4536280632019043})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.8951423168182373})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1615872383117676})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.9615001678466797})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.720705509185791})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7564878463745117})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0780153274536133})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.246771812438965})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.232107639312744})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.2733731269836426})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.1292858123779297})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.007847547531128})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.980653762817383})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.9033665657043457})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.225142002105713})
store['active_learning_steps'][7]['training']['best_epoch']=14
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6373, 'crossentropy': 3.1123921875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.6286847591400146})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.6705715656280518})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.6607441902160645})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.7328407764434814})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.6178045272827148})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6668708324432373})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.703134536743164})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.7712070941925049})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.6887421607971191})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.6705318689346313})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6630818843841553})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.607308268547058})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.7676382064819336})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.7471675872802734})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.643902063369751})
store['active_learning_steps'][7]['eval_training']['best_epoch']=12
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 7851], ['ood', 44342], ['id', 58840], ['ood', 9675], ['id', 16418]], 'labels': [-1, -1, 5, -1, 5], 'scores': [1.087138017903618, 1.9069313758579751, 2.5465452867772256, 2.9512991067628906, 3.2483844399478152]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.8630822896957397})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.2652840614318848})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.6563024520874023})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.003221273422241})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.032022476196289})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.2775771617889404})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.627, 'crossentropy': 2.84258046875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 1.6138317584991455})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.691305160522461})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.5649681091308594})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.5969862937927246})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.5965888500213623})
store['active_learning_steps'][8]['eval_training']['best_epoch']=5
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 15462], ['ood', 54810], ['id', 53234], ['id', 30845], ['ood', 15242]], 'labels': [-1, -1, 2, 6, -1], 'scores': [1.1346007454620404, 2.017361843900029, 2.588234541248052, 2.9787571769987435, 3.231426294372021]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.8681594133377075})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.46720027923584})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.7958788871765137})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0685529708862305})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.157111167907715})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1770694255828857})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.959764003753662})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6229, 'crossentropy': 2.9410787109375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.5203958749771118})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.5708909034729004})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.5810105800628662})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.509676456451416})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.5397777557373047})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.5857123136520386})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 25180], ['ood', 39944], ['ood', 21809], ['ood', 32030], ['ood', 36882]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0258418344952498, 1.7858143876432178, 2.336366482724683, 2.7042760103789205, 2.882704534856868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.663914680480957})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.1550183296203613})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.482630729675293})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.588836908340454})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.646892547607422})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.8874921798706055})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.955519199371338})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6342, 'crossentropy': 2.729941796875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5574266910552979})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.613053560256958})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4923505783081055})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.4546009302139282})
store['active_learning_steps'][10]['eval_training']['best_epoch']=1
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 23528], ['ood', 55149], ['ood', 45394], ['id', 45018], ['id', 43193]], 'labels': [-1, -1, -1, 0, 5], 'scores': [0.844823966284703, 1.487581888805558, 1.9618955128005613, 2.201950476735549, 2.352083432629735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.8102078437805176})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.099193811416626})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.4747486114501953})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.910317897796631})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.769859790802002})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.9882142543792725})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.0282387733459473})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.027503490447998})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.636, 'crossentropy': 2.9425837890625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.6255319118499756})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.571699857711792})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.5366852283477783})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.5511932373046875})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.5886447429656982})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.5852949619293213})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.471477746963501})
store['active_learning_steps'][11]['eval_training']['best_epoch']=6
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 54044], ['ood', 47699], ['ood', 8993], ['ood', 53854], ['id', 46289]], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.9381801342758604, 1.7223995748563294, 2.3844896266734814, 2.8198204644958516, 3.0538636648016864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.694993019104004})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.1082146167755127})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.583984375})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.7268619537353516})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.886669874191284})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6588, 'crossentropy': 2.375175}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3473467826843262})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2800323963165283})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.3454887866973877})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.2682921886444092})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 44769], ['ood', 2780], ['ood', 27537], ['ood', 9790], ['ood', 39427]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9960827920102642, 1.8029386725388448, 2.372366882160531, 2.757616781244187, 2.984914321679963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.637970209121704})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.131317377090454})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.3737478256225586})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.614588499069214})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.825368642807007})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.775099039077759})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.124399185180664})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 3.2397873401641846})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.9785451889038086})
store['active_learning_steps'][13]['training']['best_epoch']=6
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6572, 'crossentropy': 2.713380859375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4202879667282104})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.398333191871643})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.452815294265747})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4781427383422852})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.3047629594802856})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.386103868484497})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.3594295978546143})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.4113874435424805})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 27093], ['ood', 14692], ['ood', 3676], ['ood', 39483], ['id', 23011]], 'labels': [-1, -1, -1, -1, 0], 'scores': [1.031372491424448, 1.8340794196499353, 2.4237031341457533, 2.794183251474562, 3.006227109001317]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.6307127475738525})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.9897739887237549})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.278449058532715})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.5757393836975098})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.5199954509735107})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.75569486618042})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6686, 'crossentropy': 2.241098046875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.4158570766448975})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.480146884918213})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.3997793197631836})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.3936907052993774})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.3455047607421875})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 32799], ['ood', 41606], ['ood', 25665], ['ood', 10716], ['ood', 48880]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9732915670748237, 1.7834166130280806, 2.3822508032015532, 2.746304394970256, 2.9466710162016225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.674270510673523})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.022181987762451})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.3161935806274414})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4928555488586426})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.7018961906433105})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.9684481620788574})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6711, 'crossentropy': 2.4459115234375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.4409226179122925})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.4618690013885498})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.5008792877197266})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.397243857383728})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.446486473083496})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 27431], ['ood', 2634], ['id', 17312], ['ood', 28992], ['ood', 6484]], 'labels': [-1, -1, 8, -1, -1], 'scores': [0.9549451356194564, 1.7130187678423519, 2.1726345546599326, 2.499388798649989, 2.7272257585222945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.6134147644042969})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.2725281715393066})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.916106700897217})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.6874876022338867})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.852860927581787})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.7242352962493896})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 3.048309803009033})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.991217851638794})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 3.042529582977295})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 3.3593249320983887})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 3.1843714714050293})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.3525333404541016})
store['active_learning_steps'][16]['training']['best_epoch']=9
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.658, 'crossentropy': 3.345401953125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.5884311199188232})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.7957274913787842})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.744905710220337})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.749671220779419})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.8452847003936768})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.7572355270385742})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.8195810317993164})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.8068082332611084})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.6926853656768799})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 47426], ['ood', 2209], ['ood', 21851], ['ood', 54304], ['ood', 34304]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1305755683438365, 2.0486258979406022, 2.663450237299007, 3.0199738914630063, 3.2506367547441015]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.7287707328796387})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.3050808906555176})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.5802202224731445})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.709326982498169})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.6784729957580566})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6591, 'crossentropy': 2.2388623046875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.4326071739196777})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3192393779754639})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3014259338378906})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2411830425262451})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 36050], ['ood', 56645], ['ood', 37740], ['ood', 8268], ['ood', 9386]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9725190356299132, 1.655955482701493, 2.168355723083601, 2.4562407708093166, 2.6387651159595236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.6339902877807617})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.9968184232711792})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.4713892936706543})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.6409661769866943})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.9191994667053223})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6487, 'crossentropy': 2.30500625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.460097312927246})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.5583266019821167})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.401512861251831})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.329403281211853})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 21463], ['ood', 33727], ['ood', 51415], ['id', 36820], ['ood', 14325]], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.9453227846372828, 1.6593689815873476, 2.2308330686453735, 2.6307943622872543, 2.8273608982119827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.4599982500076294})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.946962594985962})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.2146501541137695})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.1383860111236572})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4199044704437256})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6776, 'crossentropy': 1.8858490234375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3092575073242188})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.2666735649108887})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.2031373977661133})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1727635860443115})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 39976], ['ood', 56499], ['ood', 25857], ['ood', 49448], ['ood', 28944]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0828931506331272, 1.979967982761785, 2.5931993019196007, 2.989374009302699, 3.250142682351048]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.4701099395751953})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.9240282773971558})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.3430938720703125})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.612227439880371})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.1771397590637207})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.4656147956848145})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.5158166885375977})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4593381881713867})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.526705503463745})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.647085189819336})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6853, 'crossentropy': 2.46740546875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4419814348220825})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.4826445579528809})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.4781477451324463})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.5052502155303955})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.399502158164978})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.488035798072815})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.456712245941162})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.4154062271118164})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.424344539642334})
store['active_learning_steps'][20]['eval_training']['best_epoch']=8
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 25180], ['ood', 32343], ['ood', 41043], ['ood', 30317], ['ood', 29848]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0754127097399666, 1.9354826096973876, 2.6111146731500074, 3.0887199994837173, 3.368702444814409]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.5673795938491821})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.9889910221099854})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.171307325363159})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.1921043395996094})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.3968420028686523})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.3126466274261475})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.5434324741363525})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.8000035285949707})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.716395378112793})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.7549328804016113})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6819, 'crossentropy': 2.7363056640625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.417083501815796})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.516558289527893})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.4174776077270508})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4289395809173584})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.5630438327789307})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.433417558670044})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.4444477558135986})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.4272149801254272})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.4308924674987793})
store['active_learning_steps'][21]['eval_training']['best_epoch']=7
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 51600], ['ood', 37740], ['ood', 41438], ['ood', 22742], ['ood', 22254]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1954186385366883, 1.9987374942278306, 2.6387989427951712, 3.082667536376084, 3.3406264062641364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.6709566116333008})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.0114364624023438})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.2767412662506104})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.631502628326416})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.8148128986358643})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.7328903675079346})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.749495506286621})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 3.0209250450134277})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.8592214584350586})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.679, 'crossentropy': 2.7105658203125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.3965078592300415})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4779436588287354})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.375791072845459})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3754258155822754})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.396003246307373})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.53422212600708})
store['active_learning_steps'][22]['eval_training']['best_epoch']=3
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 37148], ['ood', 32533], ['id', 33801], ['ood', 31119], ['id', 31791]], 'labels': [-1, -1, 0, -1, 9], 'scores': [1.1364765782113704, 1.981695592100185, 2.5410665644799946, 2.9079129405940978, 3.1002985834250043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.5150625705718994})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.000227689743042})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.1596927642822266})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.342655897140503})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.7728943824768066})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.651827812194824})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.7219014167785645})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.669, 'crossentropy': 2.577894140625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3978569507598877})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.4321949481964111})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.401421308517456})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.38286292552948})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.3310842514038086})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3226633071899414})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 36852], ['ood', 26412], ['ood', 42405], ['id', 10026], ['ood', 47513]], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.9323743918451917, 1.650235147951133, 2.247819384642386, 2.6456776068090777, 2.9234252468673847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.4165689945220947})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.7609977722167969})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.1902036666870117})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.348872661590576})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.551513671875})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.739078998565674})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6677, 'crossentropy': 2.3548255859375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.318065881729126})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3181792497634888})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2708561420440674})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.3051490783691406})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.3167264461517334})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 38177], ['id', 7400], ['ood', 58463], ['ood', 16218], ['id', 47864]], 'labels': [-1, 6, -1, -1, 5], 'scores': [0.8545556913193019, 1.5666348693282135, 2.1406415084481485, 2.5267089017362165, 2.786746725919225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.5353903770446777})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.0244553089141846})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.249192476272583})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.402184009552002})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.513625144958496})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.627126693725586})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.929692268371582})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.581944465637207})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.8174049854278564})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.8760268688201904})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.38262939453125})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6786, 'crossentropy': 2.618043359375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.396998405456543})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.4734954833984375})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.4251742362976074})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.4981577396392822})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.4552278518676758})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4441719055175781})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.5320558547973633})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4988784790039062})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.5118720531463623})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.5643038749694824})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 51321], ['id', 12869], ['ood', 6873], ['ood', 51227], ['id', 45736]], 'labels': [-1, 2, -1, -1, 6], 'scores': [1.096929237960118, 1.9329103564551389, 2.5936817595747725, 2.9740424004118884, 3.185640595958217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.6157324314117432})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.9854416847229004})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.303713798522949})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.338686466217041})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.409493923187256})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.525073289871216})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.6076793670654297})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.3928024768829346})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.680568218231201})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 3.167466163635254})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6699, 'crossentropy': 2.8701689453125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.3588200807571411})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.477581262588501})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.4299430847167969})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.376908779144287})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.4217197895050049})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.3876055479049683})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.455672264099121})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.4008748531341553})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.4404213428497314})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 4795], ['ood', 5606], ['ood', 19759], ['ood', 16492], ['ood', 56675]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1062505067033972, 1.9852613453089398, 2.633564210782679, 3.0599297638544223, 3.3395966169770936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3698365688323975})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.7942924499511719})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.1754608154296875})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.076026201248169})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.4219889640808105})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.5036535263061523})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.598071575164795})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.6726324558258057})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6802, 'crossentropy': 2.395002734375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.3765604496002197})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.4388096332550049})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3175747394561768})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.3063275814056396})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3765449523925781})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.3316220045089722})
store['active_learning_steps'][27]['eval_training']['best_epoch']=3
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 2805], ['ood', 38271], ['ood', 4590], ['ood', 16560], ['id', 2790]], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.7876313762964663, 1.498294987909322, 1.936032352365241, 2.194385853688738, 2.33642600581686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2583098411560059})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.748832106590271})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.1303908824920654})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.050300121307373})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.4130022525787354})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.0843100547790527})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.528061866760254})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.677849769592285})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.6651809215545654})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.6806, 'crossentropy': 2.267215234375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.191802740097046})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2092382907867432})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1860475540161133})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.1778782606124878})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1921403408050537})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.151320457458496})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.207068681716919})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 52250], ['ood', 19074], ['ood', 6506], ['id', 33127], ['ood', 15751]], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.8667570505616815, 1.595632532701159, 2.1072247244620286, 2.4122707659031994, 2.5932864229257975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.360875129699707})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.7084228992462158})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.9144378900527954})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.033717155456543})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.1075375080108643})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.121413230895996})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.248246908187866})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6909, 'crossentropy': 2.278903515625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3766868114471436})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.4881858825683594})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.409188151359558})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.36116361618042})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3886504173278809})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.349621295928955})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 20856], ['ood', 1477], ['ood', 47444], ['ood', 24577], ['ood', 24521]], 'labels': [3, -1, -1, -1, -1], 'scores': [0.8962720543083824, 1.6634640180893685, 2.23715965892195, 2.6129753565812, 2.831624220888899]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.2886736392974854})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6325337886810303})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.92060124874115})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.086707592010498})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.1889796257019043})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.2682619094848633})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.691150426864624})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.3213045597076416})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6911, 'crossentropy': 2.27097265625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2685658931732178})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2333145141601562})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.1831941604614258})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.1889476776123047})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1827423572540283})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.0949809551239014})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1666882038116455})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 48681], ['ood', 48279], ['id', 41192], ['ood', 6941], ['id', 49468]], 'labels': [-1, -1, 6, -1, 5], 'scores': [0.9604838140702536, 1.6778356552341394, 2.19231295230743, 2.594901361869459, 2.873313216450814]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.4603641033172607})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.640618085861206})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.8611860275268555})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.8734511137008667})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.0789713859558105})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.9842350482940674})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6892, 'crossentropy': 1.857655078125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.208806037902832})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.266211986541748})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.140678882598877})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2015178203582764})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1410655975341797})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 42838], ['ood', 58560], ['ood', 606], ['ood', 45840], ['id', 52824]], 'labels': [-1, -1, -1, -1, 6], 'scores': [0.8615015969043291, 1.4819117294723476, 1.9522362919887688, 2.2394636620192836, 2.405705612227087]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.334566354751587})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.50101900100708})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8988924026489258})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.9683631658554077})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.0127944946289062})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.2694530487060547})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.2696871757507324})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.3413796424865723})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.5170493125915527})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.3534390926361084})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.3445253372192383})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.2587199211120605})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.4926486015319824})
store['active_learning_steps'][32]['training']['best_epoch']=10
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6946, 'crossentropy': 2.5094521484375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.2972965240478516})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3389896154403687})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.2058695554733276})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.225315809249878})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3122587203979492})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3360364437103271})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.2905683517456055})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2672148942947388})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.227918267250061})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.2817989587783813})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.2654205560684204})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3010025024414062})
store['active_learning_steps'][32]['eval_training']['best_epoch']=11
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 3362], ['ood', 43636], ['ood', 49622], ['ood', 44848], ['ood', 46489]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0979069139991753, 1.9841954389264937, 2.64226219597439, 2.95528359728977, 3.1138900722052982]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3145382404327393})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.8154041767120361})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.8841078281402588})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.004462957382202})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.3844265937805176})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.367321491241455})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6834, 'crossentropy': 2.013911328125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2405245304107666})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1969974040985107})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1471697092056274})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1371433734893799})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1266682147979736})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 31119], ['ood', 58769], ['ood', 56488], ['ood', 56127], ['ood', 4594]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7907623979866507, 1.394864145473445, 1.9003358314024803, 2.2633150078913813, 2.4404995960081752]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1851706504821777})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.6148407459259033})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.6343529224395752})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8725281953811646})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.1052000522613525})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.0859880447387695})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.1465325355529785})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.278223991394043})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.2452101707458496})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.3544185161590576})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.4005842208862305})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6855, 'crossentropy': 2.4100857421875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2971420288085938})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3063111305236816})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.390379786491394})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3840515613555908})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.334451675415039})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.383575201034546})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.4919507503509521})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3468650579452515})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 4490], ['ood', 54507], ['ood', 56718], ['ood', 3788], ['ood', 26649]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.1398891162920153, 2.0181230955401315, 2.6003587017458054, 2.9934308762426065, 3.2231675656952015]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.3813502788543701})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.719928503036499})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.8526077270507812})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.8830167055130005})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.910069465637207})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.0254387855529785})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.0413148403167725})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.2278738021850586})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6914, 'crossentropy': 2.2036078125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2106590270996094})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.1972277164459229})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.243722915649414})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.1917335987091064})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.2259068489074707})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.1909784078598022})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.2110216617584229})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 58016], ['ood', 7768], ['ood', 30972], ['ood', 25445], ['ood', 28136]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8953703017150466, 1.601939253008458, 2.129757772518187, 2.5046649115335624, 2.7147158987456077]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3497648239135742})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.7714836597442627})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.974379301071167})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.040745735168457})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.1851181983947754})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.2169995307922363})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6804, 'crossentropy': 2.0712361328125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2035338878631592})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.154226541519165})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0893640518188477})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0869343280792236})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0283915996551514})
store['active_learning_steps'][36]['eval_training']['best_epoch']=5
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 32785], ['id', 34468], ['ood', 25714], ['ood', 29004], ['ood', 633]], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.9846678178789146, 1.7311154096093637, 2.283369376108988, 2.6203448641869183, 2.810833583500364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.3773088455200195})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.6946403980255127})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.6986002922058105})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.028585195541382})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.0877623558044434})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.2216851711273193})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.4047763347625732})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6838, 'crossentropy': 2.023587890625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3134853839874268})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.2932813167572021})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1579848527908325})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.279495120048523})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2682876586914062})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2665109634399414})
store['active_learning_steps'][37]['eval_training']['best_epoch']=3
store['active_learning_steps'][37]['acquisition']={'indices': [['ood', 6308], ['ood', 47558], ['ood', 36237], ['id', 49380], ['ood', 50846]], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.9978406682428747, 1.7787416239854552, 2.3285600516581386, 2.704063910554175, 2.944714104678104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.3293776512145996})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.5769686698913574})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.811952829360962})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.1333184242248535})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.01725697517395})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.327082633972168})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.341341733932495})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.4690592288970947})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.349320888519287})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.705963134765625})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.426039934158325})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.483126401901245})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.676450729370117})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.756046772003174})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.6221299171447754})
store['active_learning_steps'][38]['training']['best_epoch']=12
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6889, 'crossentropy': 2.8049673828125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2675580978393555})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3185172080993652})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.320550799369812})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3589086532592773})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3608248233795166})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.3855972290039062})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.4373246431350708})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3615729808807373})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.3523732423782349})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.388784646987915})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.3079731464385986})
store['active_learning_steps'][38]['eval_training']['best_epoch']=8
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 27337], ['ood', 39210], ['ood', 27243], ['ood', 2548], ['ood', 9870]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.0710401504935578, 1.8744558790150943, 2.3945473048729484, 2.7344882889827464, 2.928664761091585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4022891521453857})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.573614239692688})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.961668610572815})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.8518539667129517})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.2435104846954346})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.280320167541504})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.1761045455932617})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.313646078109741})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.277428150177002})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.543928623199463})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.4592676162719727})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6921, 'crossentropy': 2.44975859375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2444044351577759})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2641420364379883})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.3905179500579834})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2957072257995605})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.2737836837768555})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.3519444465637207})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2624781131744385})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.327981948852539})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.3133907318115234})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 4157], ['ood', 4846], ['ood', 10924], ['ood', 44736], ['id', 46863]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.9099551613137522, 1.6834564530990341, 2.254276027754956, 2.6166565258472607, 2.8483829777174807]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.2465782165527344})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5504716634750366})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.8131886720657349})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.9512248039245605})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.005612373352051})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.9163792133331299})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.1205248832702637})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.3765549659729004})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.369746685028076})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.991652488708496})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6939, 'crossentropy': 2.3179978515625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2307363748550415})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.3245599269866943})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.3295446634292603})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.34360933303833})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3516241312026978})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3894875049591064})
store['active_learning_steps'][40]['eval_training']['best_epoch']=3
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 29290], ['ood', 26831], ['ood', 14027], ['ood', 56335], ['id', 40036]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.0575123280676577, 1.862430687091212, 2.473793914787378, 2.8837360081993153, 3.1281141678437403]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.3799972534179688})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.572523593902588})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.8908097743988037})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.069601058959961})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.1376404762268066})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.3229846954345703})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.336233615875244})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.2386646270751953})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6762, 'crossentropy': 2.32430546875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.244253396987915})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.3043937683105469})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.3275790214538574})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3001880645751953})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.4274845123291016})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.2970640659332275})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.3180924654006958})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 35583], ['ood', 45612], ['id', 25897], ['ood', 5175], ['id', 28427]], 'labels': [-1, -1, 5, -1, 4], 'scores': [0.9418695470765783, 1.6746623469214348, 2.2177616088114243, 2.5652580658761455, 2.77158119558336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1948596239089966})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4503583908081055})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.6121857166290283})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.8242034912109375})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.8061957359313965})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.9097967147827148})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.923379898071289})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.3442013263702393})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.693, 'crossentropy': 2.0628076171875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.197164535522461})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.3043482303619385})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.2790157794952393})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.2142245769500732})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2673664093017578})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.2013604640960693})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1663563251495361})
store['active_learning_steps'][42]['eval_training']['best_epoch']=6
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 30454], ['ood', 1341], ['ood', 386], ['ood', 32343], ['ood', 14418]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9647812255441985, 1.8004231646424906, 2.4251978454208203, 2.7881828939989597, 3.0384975669653365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.3725879192352295})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.5928237438201904})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.7521684169769287})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.0382306575775146})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.109468698501587})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.170213222503662})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.072711944580078})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.3924617767333984})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6813, 'crossentropy': 2.202938671875}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2277727127075195})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2263703346252441})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2095353603363037})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1243517398834229})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.1591002941131592})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1162223815917969})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1204156875610352})
store['active_learning_steps'][43]['eval_training']['best_epoch']=5
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 3701], ['ood', 53358], ['ood', 48608], ['ood', 49336], ['ood', 3739]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.2190876739600867, 2.0928907598973243, 2.779507329633201, 3.2165370037230963, 3.442485748499191]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.355463981628418})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.5012940168380737})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.8230407238006592})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.8965749740600586})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.0408339500427246})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.937864899635315})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6835, 'crossentropy': 1.9028626953125}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.2143909931182861})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.139458417892456})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.101219892501831})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0401339530944824})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0588366985321045})
store['active_learning_steps'][44]['eval_training']['best_epoch']=3
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 37770], ['ood', 22944], ['id', 3895], ['id', 2369], ['ood', 29161]], 'labels': [-1, -1, 8, 5, -1], 'scores': [0.84350671154316, 1.5148953050050302, 1.9877552740775082, 2.262969905051926, 2.461539814230206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.2619715929031372})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.5554263591766357})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.7639135122299194})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.850896954536438})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.071981191635132})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.030776262283325})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.143052577972412})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6827, 'crossentropy': 1.954021484375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1955556869506836})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1886436939239502})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1458897590637207})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.085338830947876})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.1280791759490967})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0651456117630005})
store['active_learning_steps'][45]['eval_training']['best_epoch']=4
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 8812], ['ood', 30770], ['ood', 6550], ['ood', 41050], ['ood', 57234]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8543545223256039, 1.6081302881462785, 2.1617317380415693, 2.47830698438032, 2.687678835941603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.308516025543213})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.5163649320602417})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.7186992168426514})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.701195240020752})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.4321298599243164})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.9794368743896484})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.9206186532974243})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6874, 'crossentropy': 1.87231171875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1969506740570068})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1652026176452637})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1672660112380981})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1141107082366943})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1066045761108398})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1061716079711914})
store['active_learning_steps'][46]['eval_training']['best_epoch']=3
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 42112], ['ood', 51722], ['ood', 3218], ['ood', 34716], ['ood', 37078]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8545873268715652, 1.583867830646696, 2.0928474658769707, 2.4053591791542086, 2.5864403189745198]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.3076502084732056})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.5975515842437744})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.7332544326782227})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.8317480087280273})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.8646223545074463})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.098257541656494})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.9231395721435547})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.203273296356201})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.329683542251587})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.238478183746338})
store['active_learning_steps'][47]['training']['best_epoch']=7
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6993, 'crossentropy': 2.0960634765625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.2595672607421875})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2892916202545166})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.284595012664795})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.2620335817337036})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.2253820896148682})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3104166984558105})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.2752933502197266})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.3097991943359375})
store['active_learning_steps'][47]['eval_training']['best_epoch']=5
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 34871], ['ood', 5813], ['ood', 22852], ['ood', 15150], ['ood', 47571]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9325783919766529, 1.683388641367807, 2.2433115157191152, 2.6220641501860813, 2.8496222533314155]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.2881247997283936})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.4731413125991821})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.6527824401855469})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.862497091293335})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.0236732959747314})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.05452036857605})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.201533794403076})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.161130428314209})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.4210872650146484})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6881, 'crossentropy': 2.15454921875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2408666610717773})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.2368111610412598})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2216819524765015})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.2163923978805542})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.171052098274231})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.1822094917297363})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1754519939422607})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1712136268615723})
store['active_learning_steps'][48]['eval_training']['best_epoch']=5
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 53854], ['ood', 39469], ['ood', 36656], ['ood', 13524], ['ood', 48668]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.012515474548889, 1.7457027774990865, 2.3161103894693764, 2.686061297789898, 2.914963602471187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.3019163608551025})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.5808653831481934})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.775366187095642})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8459367752075195})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9734333753585815})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.0938339233398438})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.3707528114318848})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 2.1728243827819824})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.3372597694396973})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.4111227989196777})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.2880101203918457})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.297001838684082})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.5503549575805664})
store['active_learning_steps'][49]['training']['best_epoch']=10
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6909, 'crossentropy': 2.5892693359375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2341909408569336})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3134093284606934})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3744475841522217})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3477232456207275})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.3778579235076904})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.3841466903686523})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.3341845273971558})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.3337675333023071})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.2550983428955078})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.3221354484558105})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.3951692581176758})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.342078447341919})
store['active_learning_steps'][49]['eval_training']['best_epoch']=9
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 25546], ['ood', 27239], ['id', 11150], ['ood', 37073], ['id', 48379]], 'labels': [-1, -1, 2, -1, 5], 'scores': [0.9717285916086897, 1.75246386680163, 2.2930325377089584, 2.666141627365622, 2.892807258877526]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.2543184757232666})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.4286439418792725})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.7801605463027954})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.8919005393981934})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.0457661151885986})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.0105974674224854})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.1279311180114746})
store['active_learning_steps'][50]['training']['best_epoch']=4
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6835, 'crossentropy': 2.046501953125}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2458436489105225})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2158358097076416})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2060489654541016})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1928915977478027})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.263522744178772})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.1824764013290405})
store['active_learning_steps'][50]['eval_training']['best_epoch']=3
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 37650], ['ood', 11226], ['ood', 27793], ['ood', 35962], ['ood', 4221]], 'labels': [6, -1, -1, -1, -1], 'scores': [0.8798976236849454, 1.569614566203917, 2.1230029728128113, 2.444791784244643, 2.6254897130112527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.2696576118469238})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.4416440725326538})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.640615701675415})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.7614601850509644})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.932288408279419})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.993293046951294})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.3356990814208984})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.2725296020507812})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6999, 'crossentropy': 2.0021982421875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.260122537612915})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.2873518466949463})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.2167415618896484})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.21351158618927})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.2413314580917358})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.2256510257720947})
store['active_learning_steps'][51]['eval_training']['best_epoch']=3
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 17324], ['ood', 7851], ['ood', 15487], ['ood', 41999], ['ood', 4715]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.811435755104233, 1.510574799930113, 2.1374932079049165, 2.5045084094299552, 2.7298521320721143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2963569164276123})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3446989059448242})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.6184748411178589})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.9371942281723022})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.895958423614502})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.0001907348632812})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.0999889373779297})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.207063913345337})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.2697887420654297})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.1734707355499268})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.6992, 'crossentropy': 2.1920154296875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1823949813842773})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.299424648284912})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3141210079193115})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.319545865058899})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2240777015686035})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2231051921844482})
store['active_learning_steps'][52]['eval_training']['best_epoch']=3
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 39336], ['ood', 24860], ['ood', 41292], ['ood', 31735], ['ood', 2304]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8046866795190917, 1.5080966189509866, 2.0038344290674424, 2.3581136415576145, 2.610387871746256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2226600646972656})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3034512996673584})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.5706150531768799})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.7058519124984741})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.7680704593658447})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.9563088417053223})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.9576992988586426})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.200333595275879})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.977248191833496})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.9279441833496094})
store['active_learning_steps'][53]['training']['best_epoch']=7
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6993, 'crossentropy': 2.2039537109375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.3009774684906006})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.245724081993103})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3392689228057861})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.294996976852417})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.2979028224945068})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.2382361888885498})
store['active_learning_steps'][53]['eval_training']['best_epoch']=3
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 51858], ['ood', 29334], ['ood', 13259], ['id', 45570], ['ood', 53504]], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.9408495325557793, 1.7007419095932046, 2.2129308881515204, 2.552437050669606, 2.7581487693765085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.23390793800354})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.384239912033081})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.576326847076416})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.7118499279022217})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.7239688634872437})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.8664026260375977})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.007483959197998})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6929, 'crossentropy': 1.8178630859375}
